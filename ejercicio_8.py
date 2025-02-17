def promedio_notas(nota_1,nota_2, nota_3):
    resultado = nota_1 + nota_2 + nota_3
    return resultado / 3

nombre = input("Ingresa tu nombre----")
notas_matematicas = int(input("Ingresa la nota de matematicas " ))
notas_español = int(input("Ingresa la nota de español " ))
notas_ciencias = int(input("Ingresa la nota de ciencias " ))
print(f"El promedio de las notas de {nombre} es :{promedio_notas(notas_matematicas, notas_español, notas_ciencias)}")


