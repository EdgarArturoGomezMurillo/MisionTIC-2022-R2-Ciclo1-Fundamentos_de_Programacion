import json
import pandas as pd
print("\x1Bc")
# crear un dataframe
# crear dataframe apartir de un diccionario

# listado atletas
"""dict_datos = {"Nombre": ["Juan", "Pedro", "Maria"], "apellidos": ["gomez", "suarez", "laura"],
              "Edad": [20, 21, 22], "partido_1": [1, 2, 3], "partido_2": [4, 5, 6]}
# crear mi dataframe
datos_deportistas = pd.DataFrame(dict_datos)
print(datos_deportistas)
# exportar como archivo CSV
datos_deportistas.to_csv("datos_deportistas.csv")
print("datos exportados con exito")"""

# importar o leer archivos csv

"""df = pd.read_csv("datos_deportistas.csv", index_col= 0)
print(df)"""
 
#exportar excel
"""dict_datos = {"Nombre": ["Juan", "Pedro", "Maria"], "apellidos": ["gomez", "suarez", "laura"],
              "Edad": [20, 21, 22], "partido_1": [1, 2, 3], "partido_2": [4, 5, 6]}

datos_deportistas = pd.DataFrame(dict_datos)
print(datos_deportistas)
# exportar como archivo xlsx
try:
    datos_deportistas.to_excel("datos_deportistas.xlsx")
    print("datos exportados con exito")
except:
    print("error al exportar")"""
    
    #importar archivos de excel
"""df= pd.read_excel("datos_deportistas.xlsx", index_col= 0)
print(df)"""

#archivos json
#atletas recorrer 100 mts planos
import json as js
"""atletas = {}
atletas["datos_basicos"]= []
atletas["datos_basicos"].append({"nombres":"arturo", "apellidos":"gomez", "edad":20, "tiempo":5})
atletas["datos_basicos"].append({"nombres":"valeria", "apellidos":"gomez", "edad":25, "tiempo":2})
atletas["datos_basicos"].append({"nombres":"juan", "apellidos":"gomez", "edad":23, "tiempo":3})
print(atletas)

with open("atletas.json", "w") as file:
    json.dump(atletas, file, indent=2)
    print("archivo exportado con exito")"""
    
#importar JSON
with open("atletas.json") as file:
    datos = json.load(file)
    print(datos)
    
for atletas in datos["datos_basicos"]:
    print("nombre:", atletas["nombres"])
    print("apellidos:", atletas["apellidos"])
    print("edad:", atletas["edad"])
    print("tiempo:", atletas["tiempo"])
    print("-------------------------------------------------")
    
    
