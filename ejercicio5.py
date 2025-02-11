# Ejercicio
#iterar sobre un rango en especifico mayor de 100 
#Si el valor es menor que 100 no debe iterar si no mostrar un mensaje que diga que le numero debe ser mayor que 100
#Unicamente va a imprimir multiplos de 5
#Debe finalizar en 100 cerrados

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero no permitida"

print("Selecciona operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

eleccion = input("Introduce tu elección (1/2/3/4): ")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if eleccion == '1':
    print(f"La suma de {num1} y {num2} es {suma(num1, num2)}")
elif eleccion == '2':
    print(f"La resta de {num1} y {num2} es {resta(num1, num2)}")
elif eleccion == '3':
    print(f"La multiplicación de {num1} y {num2} es {multiplicacion(num1, num2)}")
elif eleccion == '4':
    print(f"La división de {num1} entre {num2} es {division(num1, num2)}")
else:
    print("Elección inválida")