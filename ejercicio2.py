# se va a declarar una variable con un numero y determinar si es primo o no
# Un numero primo solo puede tener hasta dos divisores entre si mismo y el numero uno.

numero = 9


if numero <= 1:
    print(f"{numero} Error")
elif numero == 2:
    print(f"{numero} Es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} No es primo")
            break
    
    print(f"{numero} Es primo")


# correcion
