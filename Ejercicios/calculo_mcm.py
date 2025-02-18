
def mcm(numero1, numero2, numero3): # Definimos la funcion que crea el minimo como un multiplo

    if numero1 > numero2 and numero3: 
        num_mayor = numero1
    elif numero2 > numero1 and numero3:
        num_mayor = numero2
    else:
        num_mayor = numero3

    while (num_mayor % numero1) != 0 or (num_mayor % numero2) != 0 or (num_mayor % numero3) != 0: # Mientras esta condición no se cumpla vamos aumentando num_mayor en 1
        num_mayor += 1

    return num_mayor # Seria el mcm una vez el programa lo aya encontrado

print(mcm(156, 78, 16))