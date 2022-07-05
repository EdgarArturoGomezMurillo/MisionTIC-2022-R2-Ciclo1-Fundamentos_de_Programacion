listan = range(1, 101)
for lista in range(len(listan)):
    if listan[lista] % 3 == 0:
        print("fizz")
    elif listan[lista] % 5 == 0:
        print("buzz")
    elif listan[lista] % 3 == 0 and listan[lista] % 5 == 0:
        print("fizzbuzz")