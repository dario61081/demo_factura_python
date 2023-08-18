#  creata a main window using tkinter

import tkinter as tk

from databases import Database
from forms import FormCaja, FormSucursal


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
    print("init sucursales")
    FormSucursal(db=db_instance).show()


def init_cajas():
    print("init cajas")
    FormCaja(db=db_instance).show()


def init_timbrados():
    print("init timbrados")
    # FormTimbrado(db=db_instance).show()


def init_facturas():
    print("init facturas")
    # FormFactura(db=db_instance).show()


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

    # app_icon = tk.PhotoImage(file='assets/app.png')

    root = tk.Tk()
    root.title("Factura Electronica")
    root.geometry("800x600")
    root.resizable(False, False)
    root.iconbitmap('assets/app.ico')
    root.grid_rowconfigure(0, weight=1)
    root.positionfrom('user')

    root.config(menu=MainMenu(), background='#edeff0')
    root.mainloop()


if __name__ == '__main__':
    db_instance = Database(path='database/database.sqlite')
    main()
