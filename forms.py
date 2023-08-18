import tkinter
from tkinter.ttk import Treeview

from tkutils import TkForm, TkButton, TkInput, TkLabel, TkDataGrid


class FormCaja(TkForm):

    def __init__(self, **kwargs):
        super().__init__(title='Cajas', **kwargs)

        # menu

        menu = tkinter.Menu()
        menu_acciones = tkinter.Menu(menu, tearoff=0)
        menu_acciones.add_command(label='Nuevo', command=self.save)
        menu_acciones.add_command(label='Editar', command=self.save)
        menu_acciones.add_command(label='Eliminar', command=self.save)
        menu_acciones.add_separator()
        menu_acciones.add_command(label='Salir', command=self.close)
        menu.add_cascade(label='Datos', menu=menu_acciones)
        self.menu = menu

        # mostrar datagrid
        self.add_widget(TkDataGrid(columns=['Código', 'Nombre', 'Descripción'], name='grid'))

        self.init_db()

    def init_db(self):
        grid = self.get_widget_by_name('grid')
        if isinstance(grid, Treeview):
            grid.heading('#0', text='Código')
            grid.heading('#1', text='Nombre')
            grid.heading('#2', text='Descripción')





    def save(self):
        print("saved!")

    def create(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass





class FormSucursal(TkForm):

    def __init__(self, **kwargs):
        super().__init__(title='Sucursales', **kwargs)

        # menu

        menu = tkinter.Menu()
        menu_acciones = tkinter.Menu(menu, tearoff=0)
        menu_acciones.add_command(label='Nuevo', command=self.save)
        menu_acciones.add_command(label='Editar', command=self.save)
        menu_acciones.add_command(label='Eliminar', command=self.save)
        menu_acciones.add_separator()
        menu_acciones.add_command(label='Salir', command=self.close)
        menu.add_cascade(label='Datos', menu=menu_acciones)
        self.menu = menu

        # Label: Código  Input: Codigo

        self.add_widget(TkLabel(text='Código'))
        self.add_widget(TkInput(text='Codigo'))
        self.add_widget(TkLabel(text='Nombre'))
        self.add_widget(TkInput(text='Nombre'))
        self.add_widget(TkLabel(text='Descripción'))
        self.add_widget(TkInput(text='Descripción'))
        self.add_widget(TkButton(text='Guardar', command=self.save))

    def save(self):
        pass

    def close(self):
        pass


class FormFactura(TkForm):

    def __init__(self):
        super().__init__(title='Facturas')
