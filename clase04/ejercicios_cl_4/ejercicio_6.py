import math

peso_en_kg = float(input("Escriba su peso en kg: "))
estatura_en_metros = float(input("Escriba su estatura en metros: "))


def masa_corporal(peso_en_kg, estatura_en_metros):
    indice_masa_corporal = round(peso_en_kg /math.pow(estatura_en_metros, 2),1)
    print("Tu indice de masa corporal es {}".format(indice_masa_corporal))


indice_corporal = masa_corporal(peso_en_kg, estatura_en_metros)
print(indice_corporal)
