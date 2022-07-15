
from math import floor


cajas_de_refrescos = 9
latas_de_refrescos = 24
personas = 56
total_refrescos = latas_de_refrescos * cajas_de_refrescos
cantidad_de_latas_consumidas_por_1_persona = total_refrescos / personas
cantidad_de_latas_consumidas_por_1_persona = floor(cantidad_de_latas_consumidas_por_1_persona)
total_latas_consumidas = cantidad_de_latas_consumidas_por_1_persona * personas
latas_sobrantes = total_refrescos - total_latas_consumidas
print(latas_sobrantes)
