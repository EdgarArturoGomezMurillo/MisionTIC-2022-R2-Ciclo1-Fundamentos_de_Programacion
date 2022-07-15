lista = [1,3,4,5,6,7,8,9]
def mayorlista (lista:list):
    return f"el numero mayor de la lista es : {max(lista)}"

def menorlista (lista:list):
    return f"el numero menor de la lista es : {min(lista)}"

def sumarlista (lista:list):
    return f"la suma de los numeros de la lista es : {sum(lista)}"
print(sumarlista(lista))
print(mayorlista(lista))
print(menorlista(lista))