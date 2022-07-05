import pandas as pd
import numpy as np
print("\x1Bc")
# asignaturas que ve un estudiante x
# lista o ponindo la lista directamente en los parametros de pd.series
"""asignaturas = pd.Series(["Matematicas", "Fisica", "programacion"], index=["m01", "f02", "p03"])
print(asignaturas)
 #Diccionario
 #las notas
asignaturas = pd.Series({"Matematicas":5.0, "Fisica":5.0, "programacion":5.0})
print(asignaturas)
#tuplas
asignaturas = pd.Series(("Matematicas", "Fisica", "programacion"))
print(asignaturas)"""

"""asignaturas = pd.Series(["Matematicas", "Fisica", "programacion"], index=["m01", "f02", "p03"])
asignaturas.name="nombre de la serie"
print(asignaturas)
print("tipo de datos", asignaturas.dtype)
print("indices", asignaturas.index)
print("valores", asignaturas.values)
pesos = pd.Series([10000, 300000, 4000000], index=["m01", "f02", "p03"],dtype=float)
print(pesos)"""
"""asignaturas = pd.Series({"Matematicas":5.0, "Fisica":5.0, "programacion":5.0})
print(asignaturas)
print("notas de matematicas")
print(asignaturas[0])
print("notas de fisica")
print(asignaturas[1])
print("notas por rango: fisica y programacion")
print(asignaturas[1:3])
print("index y por el valor")
print(asignaturas[[2,0,1]])
print("funcion get")
print(asignaturas.get(1))"""

"""asignaturas = pd.Series(["Matematicas", "Fisica", "programacion"], index=["m01", "f02", "p03"])
print(asignaturas)
print("por indice explicito o por etiquetas")
print(asignaturas.loc["m01"])
print("por indice inplicito")
print(asignaturas.iloc[0:3])
print("por indice inplicito solo las que queremos")
print(asignaturas.iloc[[0,2]])
print("aleatorios")
print(asignaturas.sample(2, random_state=0))
print("eliminar")
asignaturas.pop("m01")
print(asignaturas)
x = pd.Series([1,2,3,4])
x.pop(2)
print(x)
asignaturas.drop(asignaturas.index[[1]])
print (asignaturas)"""

"""x= pd.Series([1,2,3,4,5,6,7,8,9,10])
print(x>5)
print(x[x>5])
print(x.axes)
print(x.shape)"""
"""asignaturas = pd.Series(["Matematicas", "Fisica", "programacion"], index=["m01", "f02", "p03"])
print(asignaturas)
print("editar la serie")
asignaturas[1] = "español"
print(asignaturas)
asignaturas [0:2]=["spciales","español"]
print(asignaturas)
asignaturas ["m01"]="azul"
print(asignaturas)"""

"""numeros= pd.Series([1,2,3,4,5,6,7,8,9,10])
#los numeros pares
r=numeros.where(numeros%2==0)
print(r)
a=[]
for i in range(r.shape[0]):
    if not pd.isna(r[i]):
        a.append(r[i])
print(a)"""
# dataframes
# 1.crear un diccionario
"""Venta={"manzanas":[60, 10, 20, 30, 50], "peras":[10, 20, 30, 40, 50], "uvas":[20, 30, 40, 50, 60]}
#Hacer un dataframe con el diccionario
frutasvendidas= pd.DataFrame(Venta, index=["lunes", "martes", "miercoles", "jueves", "viernes"])
print (frutasvendidas)
#atributos
print("atributos de index y colums")
print("imprimir indices")
print(frutasvendidas.index)
print("imprimir columnas")
print(frutasvendidas.columns)
print("axes----- brindar info")
print(frutasvendidas.axes)
print("dimensiones")
print(frutasvendidas.shape)
print("nombre a mis filas y a mis columnas")
print("nombre de mis filas")
frutasvendidas.index.name = "dias"
frutasvendidas.columns.name = "frutas"
print(frutasvendidas)
print("los valores ")
print(frutasvendidas.values)"""
"""x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print (x)
df=pd.DataFrame(x)
print(df)"""

# crear dataframes a partir de diccionarios
"""unidades_2020 = {"hierro":5.2,"fosforo":7.2, "potasio":6.3}
unidades_2021 = {"hierro":5.4,"fosforo":7.3, "potasio":6.9}
unidades_2022 = {"hierro":5.3,"fosforo":7.5, "potasio":6.8}
elementos=pd.DataFrame([unidades_2020, unidades_2021, unidades_2022], index=[2020, 2021, 2022])
print (elementos)"""

# crear dataframes a partir de series
"""entran = pd.Series([10, 15, 24, 28, 34, 45, 56, 78, 90, 10, 11, 21], index=["enero", "febrero", "marzo",
                   "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"])

salen = pd.Series([12, 14, 14, 18, 14, 15, 16, 18, 10, 11, 14, 81], index=["enero", "febrero", "marzo",
                   "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"])

#crear el dataframe
inventario=pd.DataFrame({"entradas":entran, "salidas":salen})
print (inventario)
#agregar otra columna
inventario["saldo"]= inventario.entradas - inventario.salidas
print (inventario)
print("mostrar los primeros 10")
print(inventario.head(10))
print("mostrar los 5 ultimos")
print(inventario.tail(5))
print("mostrar 5 aleatorios")
print(inventario.sample(5))
print("informacion estadistica")
print(inventario.describe())
print("informacion basica")
print(inventario.info())"""

"""conteo = pd.Series([8,12, 15, 11, 8, 34, 8, 56, 78, 90, 10, 11, 21])
print("conteo de valores")
print(conteo.value_counts())"""


# selecccion de informacion
"""ventas = pd.DataFrame({"entradas": [23, 34, 56, 70], "salidas": [40, 30, 50, 60], "valoracion": [1, 2, 3, 6], "limite": [
                      "no", "no", "si", "si"], "cambio": [2.3, 3.3, 4.5, 4.6]}, index=["enero", "febrero", "marzo", "abril"])
print(ventas)
print("por medio de keys----columns")
print(ventas["entradas"])
print("por medio del index")
print(ventas["entradas"]["enero"])
#metodo loc y iloc
print("por medio de loc")
print(ventas.loc["enero"])
print("por medio de iloc")
print(ventas.iloc[0])
print("por medio del  get")
print(ventas.index.get_loc("abril"))

#por rango
print("por rango")
print(ventas.iloc[0:2 , 0:2])"""

# DataFrame con rango
"""df = pd.DataFrame(np.arange(1, 19).reshape(6, 3), 
                  index=["a", "b", "c", "d", "e", "f"], columns=["A", "B", "C"])
print(df)

#edicion de DataFrame

print("por los indices -----metodo iloc")
df.iloc[1,2]=-2
print(df)
print("modificar el numero 8 por -8")
df.iloc[2,1]=-8
print(df)
df["A"]=[-1,1,1,1,1,1]
print(df)
print("por filas")
df.loc["f"]=[1,3,4]
print(df)
print("con rango")
df.iloc[3:6,1:3]=-1
print(df)"""

# metodo where
"""df = pd.DataFrame(np.arange(1, 13).reshape(4 ,3),
                  index=["a", "b", "c", "d"], columns=["A", "B", "C"])

print(df)
#Numero pares
pares = df.where(df % 2 == 0)
print(pares)
#recorrido por todo el dataframe
print("dimension de pares ", pares.shape)
print("filas", pares.shape[0])
print("columnas", pares.shape[1])

rf=[]
for filas in range(pares.shape[0]):
    for columnas in range(pares.shape[1]):
        if not pd.isna(pares.iloc[filas, columnas]):
            rf.append((pares.iloc[filas,columnas]))
print(rf)"""

#eliminar por metodo drop 
"""df = pd.DataFrame(np.arange(1, 13).reshape(4 ,3),
                  index=["a", "b", "c", "d"], columns=["A", "B", "C"])
print("eliminar por filas")
print(df.drop("c"))
print("eliminar por varias filas")
print(df.drop(["a" ,"b"]))
print("aliminar por columnas")
print(df.drop(columns="B"))"""
#funcion concatenar
"""df = pd.DataFrame(np.arange(1, 13).reshape(4 ,3),
                  index=["a", "b", "c", "d"], columns=["A", "B", "C"])
df2 = pd.DataFrame(np.arange(12,24).reshape(4 ,3),
                  index=["a", "b", "c", "d"], columns=["D", "F", "G"])
dff= pd.concat([df, df2])
print(dff)"""
