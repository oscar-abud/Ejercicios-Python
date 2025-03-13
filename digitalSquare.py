valor = int(input("Ingrese el numero entero: "))

lista = []

for i in str(valor):
    lista.append(int(i))

suma = sum(lista)

while suma >= 10:
    sumaFinal = 0
    for n in str(suma):
        sumaFinal += int(n)
    suma = sumaFinal

print(f"Lista de dígitos: {lista}")
print(f"Suma final reducida a un solo dígito: {suma}")
