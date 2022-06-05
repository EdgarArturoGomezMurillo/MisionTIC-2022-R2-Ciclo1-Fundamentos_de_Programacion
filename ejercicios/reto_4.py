from functools import reduce as rd
print("\x1Bc")

def ordenes(rutinaContable):
    Nueva_factura = list(map(lambda lista: [lista[0]] + list(map(lambda tupla: tupla[1]*tupla[2], lista[1:])), rutinaContable))
    Nueva_factura = list(map(lambda lista : [lista[0]] + [rd(lambda v1,v2: round(v1+v2,2), lista[1:])],Nueva_factura))
    Minima_compra = 600000
    Nueva_factura = list(map(lambda lista : lista if lista [1] >= Minima_compra else (lista[0], lista[1] + 25000), Nueva_factura))
    print('----------------- Inicio Registro diario --------------------------')
    for lista in range(len(Nueva_factura)):
        print(f"La factura {Nueva_factura[lista][0]} tiene un total en pesos de {Nueva_factura[lista][1]:,.2f}")
    print('----------------- Fin Registro diario -----------------------------')


ordenes([
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
])
