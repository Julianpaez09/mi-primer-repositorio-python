# Tablas de multiplicar for anidado

for i in range(1,11):
    print("-------------")
    print(f"Tabla de multiplicar de el {i}")
    for j in range(1,11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print("---------------")
    print()