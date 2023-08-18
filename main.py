#  creata a main window using tkinter

import tkinter as tk

from databases import Database


class SucursalWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class CajaWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class TimbradoWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.tk_menu = MainMenu()


def init_sucursales():
    win = tk.Toplevel()
    win.title = "Sucursales"
    win.frame = SucursalWindow(win, None)
    win.frame.pack(fill=tk.BOTH, expand=True)


def init_cajas():
    pass


def init_timbrados():
    pass


def init_facturas():
    pass


class MainMenu(tk.Menu):
    def __init__(self):
        tk.Menu.__init__(self, tearoff=0)

        # menu_img = tk.PhotoImage(file='assets/menu.png')
        # exit_img = tk.PhotoImage(file='assets/exit.png')

        menu_sistema = tk.Menu(self, tearoff=0)
        menu_sistema.add_command(label="Sucursales", command=init_sucursales, accelerator="Ctrl+1")
        menu_sistema.add_command(label="Cajas", command=init_cajas, accelerator="Ctrl+2")
        menu_sistema.add_command(label="Timbrados", command=init_timbrados, accelerator="Ctrl+3")
        menu_sistema.add_command(label="Facturas", command=init_facturas, accelerator="Ctrl+4")
        menu_sistema.add_separator()
        menu_sistema.add_command(label="Salir", command=self.quit, accelerator="Ctrl+Q")
        self.add_cascade(label="Sistema", menu=menu_sistema)



def main():

    db_instance = Database(path='database/database.sqlite')

    root = tk.Tk()
    root.title = "Factura Electronica"
    root.geometry("800x600")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    root.config(menu=MainMenu())
    root.mainloop()


if __name__ == '__main__':
    main()
