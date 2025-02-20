
mi_lista = [2, 2, 1, 7, 6, 3, 6, 7, 5, 6, 45, 44, 45, 69, 74]
mi_lista_aux = []

for elemento in mi_lista:
    if elemento not in mi_lista_aux:
        mi_lista_aux.append(elemento)

print("La lista inicial es: ", mi_lista)
print("La lista sin duplicados es: ", mi_lista_aux)