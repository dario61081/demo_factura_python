import tkinter
from tkinter.ttk import Treeview


class TkForm:

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self.kwargs = kwargs
        self.title = self.kwargs.get('title', None)
        self.window_width = self.kwargs.get('width', 630)
        self.window_height = self.kwargs.get('height', 480)
        self.widgets = []
        self.menu = self.kwargs.get('menu', None)
        self.db = self.kwargs.get('db', None)
        self.paddings = self.kwargs.get('paddings', [10, 10, 10, 10])

    def add_widget(self, widget):
        self.widgets.append(widget)

    def get_widget_by_name(self, name):
        for widget in self.widgets:
            if widget.name == name:
                return widget
        return None

    def show(self):
        self.form = tkinter.Toplevel()
        self.form.title(self.title or 'Formulario')
        self.form.geometry(f"{self.window_width}x{self.window_height}")
        self.form.configure(background='#edeff0')
        self.form.iconbitmap('assets/window.ico')
        self.form.columnconfigure(0, weight=1)
        self.form.rowconfigure(0, weight=1)

        if self.menu:
            self.form.config(menu=self.menu)

        for widget in self.widgets:
            widget.build(self.form).pack()

    def init_db(self):
        pass

    def close(self):
        if self.form:
            self.form.destroy()




class TkWidget:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.name = self.kwargs.get('name', None)

    def build(self, parent):
        raise NotImplementedError


class TkLabel(TkWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, parent):
        return tkinter.Label(parent, text=self.kwargs['text'], bg='#edeff0', fg='#000000')


class TkInput(TkWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, parent):
        return tkinter.Entry(parent, bg='#edeff0', fg='#000000', **self.kwargs)


class TkButton(TkWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self, parent):
        return tkinter.Button(parent, bg='#edeff0', fg='#000000', **self.kwargs)


class TkDataGrid(TkWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = None
        self.columns = self.kwargs.get('columns', [])
        self.data = self.kwargs.get('data', [])

    def build(self, parent):
        self.grid = Treeview(parent)
        self.grid['columns'] = self.columns
        self.grid.grid_rowconfigure(0, weight=1)
        self.grid.grid_columnconfigure(0, weight=1)
        return self.grid
