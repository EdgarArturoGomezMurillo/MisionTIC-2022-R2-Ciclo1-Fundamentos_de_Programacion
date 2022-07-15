peso_en_libras = float(input("ingrese su peso en libras : "))
def peso_libras_a_kilos (peso_en_libras):
    libras_a_kilos = peso_en_libras / 2.2046
    return f"su peso en kilos es {float(round(libras_a_kilos))}"    

print (peso_libras_a_kilos(peso_en_libras))