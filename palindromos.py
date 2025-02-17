cadena = input("Porfavor introduce una frase o una palabra: " )

cadena = cadena.lower()   #Convierto cadena en minisculas

l_cadena = list(cadena)  #Convierto cadena en una lista

l_cadena_al_reves =list(cadena)
l_cadena_al_reves.reverse() #reverse invierte la cadena convertida en lista

while " " in l_cadena:
    l_cadena.remove(" ") #remove retira el espacio de cadena en caso de contener espacios mediante el bucle whilwe

while " " in l_cadena_al_reves:
    l_cadena_al_reves.remove(" ")


if l_cadena == l_cadena_al_reves: #Comprueba si l_cadena y l_cadena_al_reves son iguales
    print("Lo que escribiste es un palindromo es un palindromo")
else:
    print("Esto nooooo es un palindromo")