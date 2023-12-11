""" 
This module is function main
"""
import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    """ 
    This function is main for my APP
    """
    root = tk.Tk()
    root.title('Catalogo peliculas')
    root.iconbitmap('./images/icono-movie.ico')
    root.resizable(0, 0)
    barra_menu(root)
    app: Frame = Frame(root)
    app.mainloop()


if __name__ == "__main__":
    main()
