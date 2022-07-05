import numpy as np
print("\x1Bc")
'''m1D=np.array([1,2,3,4])
print (m1D)
print (type(m1D))
print("matriz de dos dimensiones o bidimensional o matriz de rango 2")
m2D=np.array([[1,2,3],[4,5,6]]) #2*3
print (m2D)
print("matriz de tres dimensiones o tridimensional o matriz de rango 3")
m3D=np.array([[1,2,3],[4,5,6],[7,8,9]]) #3*3
print (m3D)  
print(m2D.shape)#longitud de la matriz'''
'''m3D=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print (m3D)  
print(m3D[0,2])#entrar a los datos de la matriz '''
'''print("matriz con numeros aleatorios")
mna = np.random.random((3, 3))
print(mna)
print("matriz con numeros enteros")
mne = np.random.randint(100, 210, (3, 3))
print(mne)
print("matriz de ceros")
mceros = np.zeros((3, 3))
print(mceros)
print("matriz de 1nos")
munos = np.ones((3, 3))
print(munos)
print("matriz constante")
nc=np.full((2,3),8)
print(nc)'''
'''print("matriz identidad")
mi=np.eye(4)
print(mi)
print("rebanadas de matriz")
rm = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(rm)'''

'''print(rm[1:3, 2:3])
print("invertir filas")
print(np.fliplr(rm))
print("trasnformar filas a columnas")
print(np.transpose(rm))'''

#indexacion de Matrices
#indexar por arrays
'''a=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]]) #4 *3
print(a)
print("indexacion con un vector")
b=np.array([0,2,0,1])
print(a[np.arange(4),b])
#sumar un numero a la indexacion de Matrices
print("sumar un numero a cada numero de la matriz de indexacion")
print(a[np.arange(4),b] + 10)
print(help(np.arange))'''
#indexacion por matrices booleanas
'''print("indexacion por matrices booleanas")
a=np.array([[1,2],[3,4],[5,6]])
print(a)
matrizb=(a > 2)
print (matrizb)
print("imprimir los numeros mayores que dos")
print(a[matrizb])
# imprimir numeros 1 sola linea
print("imprimir los numeros 1 sola linea")
print(a[a>2])'''
#saber el tipo de dato que hay en mi matriz
'''x=np.array([1,2,3,4], dtype=np.int32)
print(x.dtype)'''
#operaciones con matrices
'''print("operaciones con matrices")
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x+y)
#o tambien con add
print(np.add(x,y))
print("resta de matrices")
print(x-y)
print(np.subtract(x,y))
print("producto de elementos")
print(x*y)
print(np.multiply(x,y))
print("division de elementos")
print(np.round((x/y),2))
print(np.divide(x,y))
print("raiz cuadrada")
print(np.sqrt(x))
print("multiplicacion de matriz")
print(np.dot(x,y))'''
print("Bradcasting")
print("sumar vector a cada fila de la matriz")
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([3,5,7])
y=np.empty_like(x)
for Matriz in range(4):
    y[Matriz,:] = x[Matriz,:]+v
print(y)