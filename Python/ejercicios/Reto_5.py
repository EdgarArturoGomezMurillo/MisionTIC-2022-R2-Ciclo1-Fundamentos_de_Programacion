
import pandas as pd
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'
def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split(".")[-1] == "csv?raw=true":
        try:
            archivocsv= pd.read_csv(rutaFileCsv , index_col= 0)
            subconjunto= archivocsv[["Country", "Language", "Gross Earnings"]]
            #pivot_table organiza los registros repetidos en un solo registro
            subconjuntof= subconjunto.pivot_table(index= ["Country", "Language"])
            return(subconjuntof.head(10))
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")
print(listaPeliculas(rutaFileCsv))
        