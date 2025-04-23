"""
Haz el metodo de la burbuja para ordenar una lista de números.
"""

lista = [5, 2, 9, 1, 5, 6]

def listaOrdenada(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                #Hacemos el intercambio
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array

print(listaOrdenada(lista))

#Mostrando el paso a paso del metodo burbuja.
def burbujaPasoAPaso(array):
    n = len(array)
    for i in range(n - 1):
        print(f"\nPasada {i + 1}:")
        for j in range(n - 1 - i):
            print(f"El valor de j es : {j}")
            print(f"  Comparando {array[j]} y {array[j + 1]}")
            if array[j] > array[j + 1]:
                # Intercambio
                array[j], array[j + 1] = array[j + 1], array[j]
                print(f"    => Intercambiados: {array}")
            else:
                print(f"    => No se intercambian")
        print(f"Resultado parcial: {array}")
    return array

print("\nResultado final:")
print(burbujaPasoAPaso(lista))
