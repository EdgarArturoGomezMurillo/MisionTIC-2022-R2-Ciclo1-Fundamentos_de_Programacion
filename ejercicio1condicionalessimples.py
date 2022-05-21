num = input("ingrese un numero :")
if num<0:
    num = num * (-1)
if num > 1 and num < 9:
    print(f"el numero {num} tiene 1 digito")
else:
    if num >=10 and num <= 99:
        print(f"el numero {num} tiene 2 digitos")
    else: 
        if num >=100 and num <= 999:
            print(f"el numero {num} tiene 3 digitos")