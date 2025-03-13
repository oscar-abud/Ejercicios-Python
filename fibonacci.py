# Crear un una secuencia de fibonacci y que se muestre por pantalla

n1 = 0
n2 = 1

s = n1 + n2

limite = int(input("Ingrese el número maximo: "))

while s < limite:
    print(f"{n1} + {n2} = {s}")
    n1 = n2
    n2 = s
    s = n1 + n2
print(f"{n1} + {n2} = {s} es mayor a {limite}")
print("Por ende el programa finaliza")

## Manera con un contador

num1 = 0
num2 = 1

res = num1 + num2

contador = int(input("Ingrese las veces que quiere que se repita la serie de fibonacci: "))

for i in range(contador):
    print(f"{num1} + {num2} = {res}")
    num1 = num2
    num2 = res
    res = num1 + num2