class Empleado:
    def __init__(empleado):
        empleado.nombre=input("Ingrese el nombre del empleado: ")
        empleado.sueldo=float(input("Ingrese el sueldo del empleado: "))
    def imprimir(empleado):
        print("----------------------------------------------------")
        print("Nombre: ",empleado.nombre)
        print("Sueldo: ",empleado.sueldo)
        print("----------------------------------------------------")
    def pagar_impuestos(empleado):
        if empleado.sueldo > 3000:
            print(f"El empleado {empleado.nombre} debe pagar impuestos")
        else:
            print(f"El empleado {empleado.nombre} no debe pagar impuestos")
