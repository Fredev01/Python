""" 
This module have a class for the GUI 
"""
import tkinter as tk


def barra_menu(root):
    """ 
    This function is for make all the menu
    """
    barra_menu_ = tk.Menu(root)
    root.config(menu=barra_menu_, width=300, height=300)
    menu_inicio = tk.Menu(barra_menu_, tearoff=0)
    barra_menu_.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label="Agregar nuevo registro")
    menu_inicio.add_command(label="Eliminar registro")
    menu_inicio.add_command(label="Salir", command=root.destroy)

    barra_menu_.add_cascade(label="Consultas")
    barra_menu_.add_cascade(label="Configuración")
    barra_menu_.add_cascade(label="Ayuada")


class Frame(tk.Frame):
    """ 
    This class is for make the frames in the application
    """

    def __init__(self, root=None):
        super().__init__(root, width=700, height=500)
        self.root = root
        self.pack()
        self.config(bg="#8914ba")
