import sys
import CRUD
import InterfaceGUI as GUI
import tkinter as tk
#cargar tareas
tareas = CRUD.Read()
if not(tareas):
    sys.exit(1)
    
#cargar mi ventana
m=GUI.ventanaMenuPrincipal(tareas)
#mostrar ventana
m.mainloop()