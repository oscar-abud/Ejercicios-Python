"""
Dado un arreglo desordenado de numeros enteros, encuentra el primer entero positivo (mayor que 0) que falta en la secuencia.
"""

lista1 = [3, 4, -1, 1]
#Output 2

lista2 = [1, 2, 0]
#Output 3

lista3 = [3, 4, -1, 1, 2, 7, 10]
#Output 5

def buscandoNum(arreglo):
    #Quitamos los numeros negativos
    listas = []
    for i in arreglo:
        if i > 0:
            listas.append(i)
    #Ordenamos la lista
    listas.sort()

    #Buscamos el primer numero positivo faltante
    faltante = 1
    for numero in listas:
        if numero == faltante:
            faltante+= 1
        else:
            break

    print(f"El numero faltante en la lista {arreglo} es {faltante}")

print()
buscandoNum(lista1)
print("-"*50)
buscandoNum(lista2)
print("-"*50)
buscandoNum(lista3)
print("-"*50)