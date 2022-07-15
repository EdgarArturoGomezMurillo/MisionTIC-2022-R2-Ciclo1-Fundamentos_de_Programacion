#Ejercicio 1. Condicionales Simples

#El mayor de 2 números, sin tener en cuenta si son iguales

"""a=4
b=5

if a>b:
    print(f'El número {a} es mayor que el número {b}')
else:
    print(f'El número {b} es mayor que el número {a}')"""

#El mayor de 2 números, teniendo en cuenta si son iguales

#Ejercicio No. 2 #if en secuencia

"""a=3
b=4
if a>b:
    print(f'El número {a} es mayor que el número {b}')

if a>b:
    print(f'El número {b} es mayor que el número {a}')

if a==b:
    print(f'Los números {a} y {b} son iguales')"""

#Ejercicio No. 3 #If en cascada, por ejemplo la cantidad de digitos
#de un número 

"""num=int(input('Por favor digite un número'))

if num<0:
    num=num*(-1)
if num>=0 and num<=9:
    print (f'El número {num} tiene 1 dígito ')
else:
    if num>=10 and num<=99:
        print (f'El número {num} tiene 2 dígito ')
    else:
        if num>=100 and num<=999:
            print (f'El número {num} tiene 3 dígito ')
        else:
            if num>=1000 and num<=9999:
                print (f'El número {num} tiene 4 dígito ')
            else:
                print (f'El número {num} tiene más de 4 dígitos')"""

#Condicionales anidados.... dentro de otro... condicionales elif -- else if

#Otra forma de hacer el ejercicio anterior
#elif

"""print('El mismo ejercicio con elif')
if num<0:
    num=num*(-1)
if num>=0 and num<=9:
    print (f'El número {num} tiene 1 dígito ')
elif num>=10 and num<=99:
    print (f'El número {num} tiene 2 dígito ')
elif num>=100 and num<=999:
    print (f'El número {num} tiene 3 dígito ')
elif num>=1000 and num<=9999:
    print (f'El número {num} tiene 4 dígito ')
else:
    print (f'El número {num} tiene más de 4 dígitos')"""

#Ejercicio No. 4. Variables Booleanas
#True o False

"""a=False
b=4
print(not(a))

print(f'a es igual a: {a}, b es igual a: {b}')

print('Con un and')
if a and b<0:
    print(f'El valor de a es {a} y el valor de b es: {b} ')
else:
    print('No se cumplieron las dos condiciones')
print('Con un or')
if a or b<0:
    print(f'El valor de a es {a} y el valor de b es: {b} ')
else:
    print('No se cumple ninguna de las dos condiciones')
#Ejercicio No. 5 Operadores de comparación

"""

"""a=5
b=3
print(f'Los números son: {a} y {b}')
print('Diferencia')
print(a!=b)
print('Mayor que')
print(a>b)
print('Menor que')
print(a<b)
print('Mayor o igual')
print(a>=b)
print('Menor o igual')
print(a<=b)
print('a es lo mismo que b')
print(a is b)
print('a no es lo mismo que b')
print(a is not b)
print('a es igual a b')
print(a==b)"""

#Ejercicio No. 5 "Try ---- except"

"""try:
    a=int(input('Por favor digite un número'))
except:
    print('Señor usuario usted ha digitado un dato diferente al solicitado')"""

"""try:
    temperatura_fahr=input('Ingrese la temperatura en grados Fahrenheit :')
    fahr=float(temperatura_fahr)
    cel=(fahr-32.0)*5.05/9.0
    print(cel)
except:
    print('Por favor digite opciones válidas')


try:
    cedula=input('Digite su cédula')
    longitud=len(cedula)
    print(longitud)
    if longitud>10:
        print('Su cédula no puede ser mayor a 10 dígitos o no puede contener letras')
    cedula=int(cedula)
except:
    print('No aceptado su número de cédula o no puede contener letras...')"""


#Ejercicio No. 6 "Diccionarios"

#Formas de declarar diccionario

"""diccionarioUno={101:'Calletana López', 
                102:'Maria Baleta', 
                103:'José López'}

print(diccionarioUno)

#Otra forma de declarar

diccionarioDos={}
diccionarioDos['nota1']=3.5
diccionarioDos['nota2']=4.0
diccionarioDos['nota3']=3.2

print(diccionarioDos)

print(diccionarioUno[101])
suma=diccionarioDos['nota1']+diccionarioDos['nota2']+diccionarioDos['nota3']
print('La suma es: ', suma)

diccionarioUno[101]='Cayetana López Baleta'

diccionarioUno[104]='Juan Valdez'
print(diccionarioUno)

print('Iterando con un for ambos, clave y valor')

for key, value in diccionarioUno.items():
    print(key, value)

print('Iterar sólo por la clave')

for key in diccionarioDos.keys():
    print(key)

print('Iterar sólo por el valor')

for valor in diccionarioUno.values():
    print(valor)"""

#Ejercicio No. 7 "Promedio de notas con diccionarios"
def reporteNotas(dicInformacion):
    return f'El estudiante {dicInformacion["nombre"]} tiene un promedio de: {dicInformacion["promedio"]}'
def promedioNotas(dicNotas:dict):
    sumatoria=0
    sumatoria+=dicNotas['nota1']
    sumatoria+=dicNotas['nota2']
    sumatoria+=dicNotas['nota3']
    sumatoria+=dicNotas['nota4']
    promedio=round(sumatoria/4,2)

    dicInformacion={'nombre':dicNotas['nombre'], 'promedio':promedio}

    return dicInformacion

dicNotas={}
dicNotas['nombre']='Calletana López Baleta'
dicNotas['nota1']=3.04646465
dicNotas['nota2']=4.046545646
dicNotas['nota3']=5.0464654
dicNotas['nota4']=2.46545646546

print(reporteNotas(promedioNotas(dicNotas)))






