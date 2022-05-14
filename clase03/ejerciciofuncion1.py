nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")


def saludo(nombre):
    print("hola: ", nombre)


saludo(nombre)


def nombre_completo(nombre, apellido):
    completo = nombre + " " + apellido
    return completo
name = nombre_completo(nombre, apellido)
print (name)