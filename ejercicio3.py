# Ejercicio3
# Iterar sobre 100 numeros pero solo imprimir los que son primos
num = 1

while num <=100:
    c=1
    x=0
    while c <= num:
        if num%c==0:
            x = x+1
        c = c+1
    if x == 2:
        print(num)
       

    num = num+1
