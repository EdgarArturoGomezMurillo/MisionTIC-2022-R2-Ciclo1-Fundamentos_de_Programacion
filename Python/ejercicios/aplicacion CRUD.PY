#paso numero 3
#inicializador de tareas
tareas={
    "01":{
        "descripcion":"ir a mercar",
        "estado":"pendiente",
        "tiempo":60
    },
    "02":{
        "descripcion":"estudiar",
        "estado":"pendiente",
        "tiempo":180
    },
    "03":{
        "descripcion":"Hacer ejercicio",
        "estado":"pendiente",
        "tiempo":50
    }
}
def adicionar_tarea(tareas,identificador,nueva_tarea):
            tareas[identificador]=nueva_tarea
            return tareas
def consultar_tareas(tareas):
    for identificador, tarea in tareas.items():
        print(identificador,"--", end="")
        for atributo in tarea.values():
            print(atributo,"--",end="")
        print()
def actualizar_tarea(tareas, identificador):
    nueva_descripcion=str(input("Nueva descripcion: "))
    nuevo_estado =str(input("Nuevo estado: "))
    nuevo_tiempo =str(input("Nuevo tiempo: "))
    tareas[identificador]["descripcion"]=nueva_descripcion
    tareas[identificador]["estado"]=nuevo_estado
    tareas[identificador]["tiempo"]=nuevo_tiempo
def buscar_identificador(identificador, tareas):
    conjunto_identificadores=set(tareas.keys())
    if identificador in conjunto_identificadores:
        return True
    else:
        return False
def eliminar_tarea(tareas, identificador):
    conjunto_identificadores=set(tareas.keys())
    if identificador in conjunto_identificadores:
        #pop... elimar un elemento de mi diccionario
        tareas.pop(identificador)
        print(f'La tarea con identificador {identificador} ha sido eliminado')
    else:
        print('No existe una tarea con ese identificador')
    
#hacer menu de opciones
menu_opciones = True
while menu_opciones:
    print("----------------------------Aplicación CRUD------------------------------------\n"
          "1. Adicionar tarea - C\n"
          "2. Consultar Tareas - R\n"
          "3. Actualizar Tarea - U\n"
          "4. Eliminar Tarea - D\n"
          "5. Salir")
#Hacer validas las opciones
    opcion=int(input("digite la opcion: "))
    if opcion==1:
        print("----------------Adicionar tarea---------------")
        identificador=str(input("ingrese el indentificador de la tarea: "))
        descripcion=str(input("ingrese la descripcion de la tarea: "))
        estado=str(input("ingrese el estado de la tarea: "))
        tiempo=str(input("ingrese el tiempo de realizacion: "))
        nueva_tarea={
            "descripcion":descripcion,
            "estado":estado,
            "tiempo":tiempo
        }
        tareas=adicionar_tarea(tareas,identificador,nueva_tarea)
    elif opcion==2:
        print("----------------Consultar tareas--------------")
        consultar_tareas(tareas)
    elif opcion==3:
        print("----------------Actualizar tarea--------------")
        identificador=str(input("digite el identificador de la tarea a actualizar: "))
        if buscar_identificador(identificador, tareas):
            actualizar_tarea(tareas, identificador)
        else:
            print("no se ha encontradouna tarea con ese identificador...")
    elif opcion==4:
        print("---------------Eliminar tarea----------------") 
        identificador=str(input('Digite el identificador de la tarea a eliminar: '))
        eliminar_tarea(tareas,identificador)       
    elif opcion==5:
        print("Ha salido correctamente del sistema....")
        menu_opciones=False
    else:
        print("No ha elegido una opcion valida")
 
          