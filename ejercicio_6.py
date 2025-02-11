# Ejercicio
#iterar sobre un rango en especifico mayor de 100 
#Si el valor es menor que 100 no debe iterar si no mostrar un mensaje que diga que le numero debe ser mayor que 100
#Unicamente va a imprimir multiplos de 5

rango = int(input("Ingresa un numero mayor que cien:  "))
i = 0
# if rango <= 100:
#         print("El numero debe ser mayor que cien")
#         rango = int(input("Ingresa un numero mayor que cien   "))
# else:
#     for numero in range(100,rango + 1, 5):
#         print(numero)



if rango <= 100:
        print("El número debe ser mayor que 100")
else:
    i = 101
    while i <= rango:
        if i % 5 == 0:
            print(i)
        i = i + 1              





      




