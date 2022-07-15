#Mensajes de vienvenida por consola
def saludo():
    print("-----------------------------------------")
    print("Bienvenido a la aplicacion")
    print("-----------------------------------------")    
def despedida():
    print("-----------------------------------------")
    print("Cierre exitoso")
    print("-----------------------------------------")
#presentar mensaje generico en pantalla
def mensaje(info=""):
    print()
    print(info)
    print()
#menu rutinas tortuga
def FormularioMenuAppTortuga():
    print(" ")
    print("-- Aplicación Tortuga (Comportamiento de Objetos) ---")
    print("1. Dibujado Líneas Discontinuas")
    print("2. Polígono Irregular de 4 Lados sin Relleno")
    print("3. Polígono Irregular de 4 Lados con Relleno")
    print("4. Polilínea Ingresando Coordenadas")    
    print("5. Salir")
#Capturar la opción validando el tipo de dato para retornarlo al controlador
    opcion = None
    while opcion == None:
        try:
            opcion = int(input("Elija una rutina: "))
        except:
            print("Entrada no valida: Deve ingresar una opcion numerica")
    return(opcion) 
#recolectar cordenadas
def RecojerCordenadasTeclado():
    return int(input("Ingrese x: ")), int(input("Ingrese y: "))
#recojer por teclado el criterio de parada y retornar estado
#(True -> Continuar, False -> Detenerse)
def ControlParada():
    estado=True
    if input("desea salir? (s): ").lower()== "s":
        estado=False
        return estado