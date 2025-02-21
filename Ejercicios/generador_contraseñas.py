
import random, string

caracteres = list(string.ascii_letters + string.digits + "!#@%&*")

letras = list(string.ascii_letters)
numeros = list(string.digits)
especiales = list("!#@%&*")

tam = int(input("Por favor, introduce un tamaño para la contraseña: "))


if tam < 6 or tam > 16:
    print("Error introduce un tamaño razonabel")
else:
    random.shuffle(caracteres)

    pasword = []

    pasword.append(random.choice(letras))
    pasword.append(random.choice(numeros))
    pasword.append(random.choice(especiales))
               
            
    for i in range(tam -3):
        pasword.append(random.choice(caracteres))

    random.shuffle(pasword)

    print("".join(pasword))