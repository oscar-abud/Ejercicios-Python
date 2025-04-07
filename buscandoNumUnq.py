## Dentro de un arreglo encuentro el/los numeros que nunca se repiten dentro de la lista.

lista = [1,2,3,1,0,4,7,1,8,2,7,3,4,8,1,7,6]

#Creando una lista para los numeros unicos
num_unicos = []

print("Con el metodo count")
for numero in lista:
    # .count() funciona retorna el numero de veces que x dentro de count se encuentra en la lista.
    if lista.count(numero) == 1:
        num_unicos.append(numero)

for i in num_unicos:
    print(f"El {i} es un número unico.")


"""
Otra forma de hacerlo
"""

print("Sin el metodo count con lista.")
lista_unica = []

for i in lista:
    contador = 0
    for j in lista:
        if i == j:
            contador += 1
    if contador == 1:
        lista_unica.append(i)

for i in lista_unica:
    print(f"El {i} es un número unico")


"""
Otra forma de hacerlo
"""
from collections import Counter

print("Con diccionario.")
contador = Counter(lista)

for numero, veces in contador.items():
    if veces == 1:
        print(f"El {numero} es un número unico.")