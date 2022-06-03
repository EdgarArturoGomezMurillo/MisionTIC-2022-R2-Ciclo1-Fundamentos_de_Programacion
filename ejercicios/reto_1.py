#from typing import final


usuario_CDT = str(input("Ingrese el nombre del usuario: "))
capital_ingresado = int(input("Ingrese el dinero ingresado por el usuario: "))
tiempo_en_meses = int(input("Ingrese el tiempo que lleva el usuario en el CDT: "))

def CDT (usuario_CDT, capital_ingresado, tiempo_en_meses):
    valor_intereses =(capital_ingresado * 0.03 * tiempo_en_meses)/12
    valor_a_perder = capital_ingresado * 0.02
    if tiempo_en_meses > 2:
        valor_total = valor_intereses + capital_ingresado       
    else:
        valor_total = capital_ingresado - valor_a_perder
    print("Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario_CDT, capital_ingresado, tiempo_en_meses, valor_total))
final_CDT = CDT(usuario_CDT, capital_ingresado, tiempo_en_meses)
print (final_CDT)

