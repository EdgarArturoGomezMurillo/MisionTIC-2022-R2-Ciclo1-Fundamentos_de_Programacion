from re import M
from turtle import color
import CRUD
import tkinter as tk
from tkinter import *
def ventanaMenuPrincipal(tareas):
    #creo la ventana
    
    m=tk.Tk()
    m.title("CRUD Tareas")
    m.geometry("800x600")
    #frame de la tabla
    marcoTabla=Frame(m,borderwidth=2)
    marcoTabla.config(width="600",height="300")
    marcoTabla.config(bg="blue")
    
    marcoTabla2=Frame(m,borderwidth=2)
    marcoTabla2.config(width="600",height="300")
    marcoTabla2.config(bg="#B0E0E6")
    
    marcoTabla3=Frame(m,borderwidth=2)
    marcoTabla3.config(width="200",height="300")
    marcoTabla3.config(bg="#ADD8E6")
    
    marcoTabla4=Frame(m,borderwidth=2)
    marcoTabla4.config(width="200",height="300")
    marcoTabla4.config(bg="#87CEFA")
    #mostrar
    marcoTabla.grid(row=0,column=0,columnspan=2,rowspan=2)
    marcoTabla2.grid(row=2,column=0,columnspan=2,rowspan=2)
    marcoTabla3.grid(row=0,column=2,columnspan=2,rowspan=2)
    marcoTabla4.grid(row=2,column=2,columnspan=2,rowspan=2)
    return m
 