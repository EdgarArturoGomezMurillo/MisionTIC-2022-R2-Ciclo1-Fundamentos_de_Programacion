#Ejercicio No. 1 "Variables de incremento y de decremento"

"""i=3
#Incrementando
i=i+1#4
i+=1#5
#Decrementando
i=i-1#4
i-=1#3

print(i)"""

#Ejercicio No. 2. While.

"""n=5

while n>0:#True#True#True#True#True#False
    print(n)#5#4#3#2#1
    n-=1#4#3#2#1#0
print('Se acabó el while')"""

#Ejercicio No. 3 . While con else

#promedio=0.0
#total=0
#contar=0
"""promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))#3
while grado != -1:#True#True#False
    total = total + grado#3+8
    contar += 1#1#2
    grado = int(input(mensaje))#5#-1
else:
    promedio = total / contar#4
    print("Promedio de notas del grado escolar: " + str(promedio))#4"""

#Ejercicio No. 4 Sentencias break y continue

"""variable = 10

while variable > 0:#True#True#True#True#True
    print('Actual valor de variable:', variable)#10#9#8#7#6
    variable = variable -1#9#8#7#6#5
    if variable == 5:#False#False#False#False#True
        break"""

#Ejercicio No. 5 Sentencia continue

"""variable = 10

while variable > 0:#True#True#True#True#True#True#True#True#True#True#False
    variable = variable -1#9#8#7#6#5#4#3#2#1#0
    if variable == 5:#False#False#False#False#False#False#False#False#False
        continue
    print('Actual valor de variable:', variable) # no imprime el 5#9#8#7#6#4#3#2#1#0"""

#Ejercicio No. 6 Ciclo for

"""rango=range(1,6)

for i in rango:
    print(i)

cadenaString='Calletana'

for letra in cadenaString:
    print(letra)

for i in range(2,11,2):
    print(i)

print('Imprimir los número impares del 0-10')

for i in range(1,11,2):
    print(i)

frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombreFruta, color in frutas.items():
    print(nombreFruta, "es de color", color)

print('Iterar sólo por los key')
for nombreFruta in frutas.keys():
    print(nombreFruta)

for colorFruta in frutas.values():
    print(colorFruta)"""

#Ejercicio No. 7 "Listas"

"""lista = [1, 2.5, 'DevCode', [5,6] ,4,1,2.5]
        #[0]#[1]    #[2]     #3    #4
        #                   3,0#3,1   
print(lista)

print(lista[1])
print(lista[3])
print(lista[3][1])
print(lista[1:4])
print(lista[0:5:2])


lista2=[]
print(lista2)
print('La longitud de la lista')
print(len(lista))
print('El último elemento de la lista')
print(lista[-1])

longitudLista=len(lista)

print('El último elemento con len')
print(lista[longitudLista-1])


#Método append()

print('Lista antes de append', lista)
lista.append('Ky')
print('Lista después de agregar un último elemento', lista)

#Método count()

print(f'La cantidad de veces que aparece el número uno es: {lista.count(1)}')

#Método extend()

lisAdicional=['Esto se agregó después', 'Y esto también']

lista.extend(lisAdicional)

print(lista)

#Método index()

print(f'El índice del número 2.5 en la lista es: {lista.index(2.5)} ')

#Método insert()

print(lista)
lista.insert(1, 4.8)

print(f'La nueva lista es: {lista}')

#Método pop()
print(f'Éste es el último elemento de la lista: {lista.pop()} ')

print(f'Nueva lista con pop: {lista}')

#Método remove()

lista.remove(2.5)

print(f'La nueva lista con remove: {lista}')

#Método reverse()

lista.reverse()

print(f'Lista con reverse : {lista}')

#Método sort()


listaEnteros=[5,6,7,1,4,8]
print('Lista de Enteros', listaEnteros)
listaEnteros.sort()

print(f'La nueva lista de enteros ordenada con sort: {listaEnteros}')
listaEnteros.reverse()
print(f'Nueva lista ordenada descendentemente aplicando un reverse {listaEnteros}')"""

#Ejercicio No. 8 "Listas paralelas"

nombres=[]
edades=[]

rango=range(0,5)

#for i in range(0,5)
#for i in range(5)
"""for i in rango:
    nombre=input('Por favor digite su nombre: ')
    edad=int(input('Por favor digite su edad: '))
    nombres.append(nombre)
    edades.append(edad)

print('Las personas mayores de edad son:')

for i in rango:
    if edades[i]>=18:
        print(nombres[i])"""

#Ejercicio No. 9 " Listas Compuestas "

"""lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(lista)

#imprimir las listas internas ... 

print(lista[2])

#imprimir los componentes de las listas internas

print(lista[3][1])

#imprimir todos los componentes de las listas internas

rango=range(len(lista[3]))
for i in rango:
    print(lista[3][i])

#imprmir todos los elementos
print('Todos los elementos')
rango=range(len(lista))

for i in rango:
    for j in range(len(lista[i])):
        print(lista[i][j])"""

#Ejercicio No. 10 "Listas compuestas"

"""padres=[]
hijos=[]

rango=range(0,3)

for i in rango:
    nombrePadre=input('Digite el nombre del Padre: ')
    nombreMadre=input('Digite el nombre de la madre: ')
    padres.append([nombrePadre,nombreMadre])
    cantHijos=int(input('Por favor digite la cantidad de hijos del hogar: '))
    hijos.append([])
    for j in range(cantHijos):
        nombreHijo=input('Nombre del hijo(a) : ')
        hijos[i].append(nombreHijo)

print('Listado de papitos, mamitas e hijos')
for i in range(3):
    print(f'Nombre Padre: {padres[i][0]}')
    print(f'Nombre Madre: {padres[i][1]}')
    for j in range(len(hijos[i])):
        print(f'Nombre Hijo(a): {hijos[i][j]}')

print('Listado de padre y cantidad de hijos ')

for i in range(0,3):
    print(f'Nombre Padre: {padres[i][0]}')
    print(f'La candidad de hijos: {len(hijos[i])} ')"""

#Ejercicio No. 11 "Tuplas"
#Dict --- {key:value}
#List --- [1,2,3,4]
#Tuplas --- (1,2,3,4) ó 1,2,3,4

"""tupla=(1,2,3,4,5,4)
tupla1=1,2,3,4

print(type(tupla))
print(type(tupla1))

tuplaLetras='a','e','i','o','u'

tuplaUnElemento='a',
print(tuplaLetras)

print(type(tuplaUnElemento))

print(tupla[0])

#Tuplas son inmunables

#tupla[0]=2

#Utilizar lista de tuplas con diccionarios

diccionario = {1020:10, 'b':1, 'c':22}
print(diccionario)
t = list(diccionario.items()) #items(), devuelve una lista de tuplas
print(t)

#Métodos
print(tupla)
#Método count()

print(f'La cantidad de veces que aparece el cuatro es: {tupla.count(4)}')

#Método index()

print(f'El índice del número 2: {tupla.index(2)}')"""


#Ejercicio tipo reto 3

def AutoPartes(ventas:list):
    dic={}
    for i in range(len(ventas)):
        dic[i]=[ventas[i]]
    return dic


print(AutoPartes([
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
   

#consultaRegistro(AutoPartes([.........]))































