from tkinter import Y
import matplotlib.pyplot as plt

#crear las listas con los datos de los ejes
"""x=["reto 1", "reto 2", "reto 3", "reto 4", "reto 5"]
y = [2.5,3.5,4,1,2]

plt.plot(x,y, color = "red", linewidth = 5 , label = "tiempos retos")

#caracteristicas

plt.title="Tiempos de realizacion de retos"
plt.xlabel = "retos"
plt.ylabel = "tiempos"

#imprimir
#leer, ejes, construir una grid, imprimir
plt.legend()
plt.grid()
plt.show()"""

#dos graficas de lineas

"""x=["reto 1", "reto 2", "reto 3", "reto 4", "reto 5"]
y70 = [2.5,3.5,4,1,2]
y30= [2.7,3.0,3,2,3]
plt.plot(x,y70, color = "red", linewidth = 5 , label = "tiempos retos grupo 70")
plt.plot(x,y30, color = "blue", linewidth = 5 , label = "tiempos retos grupo 30")
#caracteristicas

plt.title="Tiempos de realizacion de retos"
plt.xlabel = "retos"
plt.ylabel = "tiempos"

#imprimir
#leer, ejes, construir una grid, imprimir
plt.legend()
plt.grid()
plt.show()"""

#Graficas de barras

"""x70=[1,2,3,4,5]
x30=[1.5,2.5,3.5,4.5,5.5]
y70 = [2.5,3.5,4,1,2]
y30= [2.7,3.0,3,2,3]
plt.bar(x70,y70, color = "red", width = 0.3 , label = "tiempos retos grupo 70")
plt.bar(x30,y30, color = "blue", width = 0.3 , label = "tiempos retos grupo 30")
#caracteristicas

plt.title="Tiempos de realizacion de retos"
plt.xlabel = "retos"
plt.ylabel = "tiempos"

#imprimir
#leer, ejes, construir una grid, imprimir
plt.legend()
plt.grid()
plt.show()"""

#histograma tarea
datos = [1,2,3,4,5,6,7,8,9,10]
rangobin= [0,10,20,30,40]
plt.hist(datos, rangobin, histtype="bar" ,color = "red", rwidth=0.8)
plt.title("histograma")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid()
plt.show()
 
#Grafico de barras con un archivo -- caracter especial r y poner \\
import pandas as pd

"""df = pd.read_csv("titanic3.csv")
print (df)
cantidad = df.survived.value_counts()
print("cantidad de muertos : ", cantidad[0])
print("cantidad de vivos : ", cantidad[1])

x = ["sobrevivientes"]
y = [cantidad[1]]

x2 = ["muertos"]
y2 = [cantidad[0]]

plt.bar(x,y, color = "red", width = 0.3 , label = "sobrevivientes")
plt.bar(x2,y2, color = "blue", width = 0.3 , label = "muertos")
#caracteristicas

plt.title="Tiempos de realizacion de retos"
plt.xlabel = "retos"
plt.ylabel = "tiempos"
plt.xticks(range(0,2))
#imprimir
#leer, ejes, construir una grid, imprimir
plt.legend()
plt.grid()
plt.show()"""


 


