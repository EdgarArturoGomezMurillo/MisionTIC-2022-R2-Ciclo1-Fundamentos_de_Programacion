Datos_del_cliente= {"Nombre": "Juan", "Apellido": "Perez", "Edad": "20", "DNI": "12345678"}
clave: Datos_del_cliente.keys()
valor:Datos_del_cliente.values()

cantidad_datos = Datos_del_cliente.items()
for clave, valor in cantidad_datos: 
    print (clave  + ":" + valor)