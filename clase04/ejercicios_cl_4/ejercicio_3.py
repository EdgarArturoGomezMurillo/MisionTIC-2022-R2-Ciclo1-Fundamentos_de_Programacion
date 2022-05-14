valor_pagar_sin_iva = input("Escriba el valor de la factura : ")
valor_pagar_sin_iva = int(valor_pagar_sin_iva)
iva = input("Escriba el porcentaje de iva a aplicar si no sabe cual es el porcentaje de iva ponga (0) : %")
iva = int(iva)
iva_decimal = iva / 100
iva_decimal = float(iva_decimal)


def total_a_pagar(valor_pagar_sin_iva, iva_decimal):
    if iva_decimal > 0:
        aplicar_iva = (valor_pagar_sin_iva * iva_decimal) + valor_pagar_sin_iva
    else:
        aplicar_iva = (valor_pagar_sin_iva * 0.19) + valor_pagar_sin_iva           
    print(("el valor total a pagar es :{} ".format(aplicar_iva)))

total = total_a_pagar(valor_pagar_sin_iva, iva_decimal)
print(total)
