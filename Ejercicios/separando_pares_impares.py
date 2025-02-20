
def separar_pares_impares(lista_entrada):
    lista_pares, lista_impares = [], []

    for numero in lista_entrada:
        # Caso de que el numero se par:
        if (numero % 2) == 0:
            lista_pares.append(numero)

        # Caso de que el numero se impar:
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares
    
mi_lista = [2, 3, 5, 8, 7, 9, 6, 12, 15, 45, 65, 32, 33, 78, 98]

print("La lista inicial es ", mi_lista)

lista_pares, lista_impares = separar_pares_impares(mi_lista)

lista_pares.sort()


print("La sublista de numeros pares es ", lista_pares)
print("La sublista de numeros impares es ", lista_impares)