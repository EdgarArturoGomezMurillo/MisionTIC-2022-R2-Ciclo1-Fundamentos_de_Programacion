import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()
#todo debe mostrarce
ventana.geometry("800x400")
ventana.title("mi primera ventana")
boton1=ttk.Button(ventana, text="Hola")
boton1.pack()

ventana.mainloop()  