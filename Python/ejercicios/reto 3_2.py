def AutoPartes(Ventas: list):
    diccionario = {}
    for tupla in Ventas:
        if diccionario.get(tupla[0]):
            diccionario[tupla[0]].append((tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6],tupla[7]))
        else:
            diccionario[tupla[0]] = []
            diccionario[tupla[0]].append((tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6],tupla[7]))
    return diccionario

def consultaRegistro(Ventas:dict, idProducto:int):
    if Ventas.get(idProducto):
        for tupla in Ventas.get(idProducto):
            print(f"Producto consultado : {idProducto}  Descripción  {tupla[0]}  #Parte  {tupla[1]}  Cantidad vendida  {tupla[2]}  Stock  {tupla[3]}  Comprador {tupla[4]}  Documento  {tupla[5]}  Fecha Venta  {tupla[6]}")
    else:
        print("No hay registro de venta de ese producto")

consultaRegistro(
    AutoPartes(
        [
        (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
        (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
        (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
        (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
        (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
        ]
    )
    , 2010)
