import json
#Consultar la información de todas las tareas (Read)
def Read(rutaArchivo=r'C:\\Users\\artur\\Misiontic\\MisionTIC-2022-R2-Ciclo1-Fundamentos_de_Programacion\\EjemploPOO\\AplicacionCRUDGUI\\listadoTareas.json'):

    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)    
    diccionarioTareas = {}#Contenedor del listado de tareas que gestiona la App
    try:    
        with open(rutaArchivo) as archivo:
            diccionarioTareas = json.load(archivo)
    except:
        print("No se pudo cargar la información de la capa de datos")
        return False #Reportar fallo en la carga

    #Retornar el contenedor o colección obtenido
    return diccionarioTareas