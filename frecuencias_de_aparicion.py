
cadena = input("Por favor, intruducir una cadena de caracteres: ") # Opción al usuario para introducir texto

cadena = cadena.lower() # Convierto cadena en minusculas

cadena = list(cadena) # Convierto cadena en una lista

while " " in cadena:
    cadena.remove(" ")  # Bucle while para retirar espacios en los textos

caracteres = {} # Creo un diccionario con el nombre de caracteres

for caracter in cadena:   # Inicio bucle for 

    if caracter in caracteres.keys(): # El método .keys() devuelve una vista de todas las claves en el diccionario.
        caracteres[caracter]+= 1 # Aumentamos el contador
    else:
        caracteres[caracter] = 1 # Si no esta en ell diccionario es la primera vez que lo encontramos y tiene frecuencia 1

print(caracteres)

