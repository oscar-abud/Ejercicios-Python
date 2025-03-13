## Dentro de un arreglo encuentro el/los numeros que nunca se repiten dentro de la lista.

lista = [1,2,3,1,0,4,7,1,8,2,7,3,4,8,1,7,6]

#Creando una lista para los numeros unicos
num_unicos = []

for numero in lista:
    # .count() funciona retorna el numero de veces que x dentro de count se encuentra en la lista.
    if lista.count(numero) == 1:
        num_unicos.append(numero)

for i in num_unicos:
    print(f"El {i} es un numero unicos.")

