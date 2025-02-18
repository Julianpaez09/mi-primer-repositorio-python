
def calcular_imc(altura, peso):

    return peso / (altura**2)


altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

imc = calcular_imc(altura, peso)

print("{:.2f}".format(imc))

if imc < 18.5:
    print("Peso insuficiente")
elif imc >= 18.5 and imc < 24.9:
    print("Peso saludable")
elif imc >= 24.9 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 29.9 and imc < 34.9:
    print("Obesidad")
else:
    print("Obesidad morbida")

