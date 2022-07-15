vueltas_por_minuto_spinner = 147
minuto_en_segundos = 60
segundos=640
vueltas_por_segundo_spinner = vueltas_por_minuto_spinner / minuto_en_segundos
vueltas_en_640_segundos = vueltas_por_segundo_spinner * segundos
vueltas_en_640_segundos = round(vueltas_en_640_segundos)
print("En 640 segundos el Fidget Spinner da:", vueltas_en_640_segundos , "vueltas")