import math as m
numero = input("escriba un numero (entero) positivo : ")

def solucion(numero):
    numero = int(numero)
    return(m.factorial(numero))
factorial = solucion(numero)
print("El Factorial de {} es: {}".format(numero, factorial))