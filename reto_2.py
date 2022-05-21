informacion = {}
informacion ["nombre"] = "arturo"
informacion ["edad"] = 7
informacion ["primer_ingreso"] = True


def cliente(informacion):
    dict_clientes = {}
    # xtreme
    if informacion["edad"] > 18:
        dict_clientes["atraccion"] = "X-Treme"
        dict_clientes["apto"] = True
        if informacion["primer_ingreso"] == True:
            dict_clientes["total_boleta"] = 19000.0
        else:
            dict_clientes["total_boleta"] = 20000
    # carroschocones
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
        dict_clientes["atraccion"] = "Carros chocones"
        dict_clientes["apto"] = True
        if informacion["primer_ingreso"] == True:
            dict_clientes["total_boleta"] = 4650.0
        else:
            dict_clientes["total_boleta"] = 5000
    # sillas voladoras
    elif informacion["edad"] >= 7 and informacion["edad"] < 15:
        dict_clientes["atraccion"] = "Sillas voladoras"
        dict_clientes["apto"] = True
        if informacion["primer_ingreso"] == True:
            dict_clientes["total_boleta"] = 9500.0
        else:
            dict_clientes["total_boleta"] = 10000
    else:
        dict_clientes["atraccion"] = "N/A"
        dict_clientes["apto"] = False
        dict_clientes["total_boleta"] = "N/A"
    nuevo_dict = {"nombre":informacion["nombre"] ,"edad":informacion["edad"] , "atraccion":dict_clientes["atraccion"], "apto":dict_clientes["apto"], "primer_ingreso":informacion["primer_ingreso"], "total_boleta":dict_clientes["total_boleta"],}
    return nuevo_dict
print (cliente(informacion))
               
           
            
    