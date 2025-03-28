'''
Obten el numero mas grande dentro de una lista. Solo se puede utilizar un ciclo for y no ocupar el metodo sort
'''

lista = [4, 2, 6, 8, 4, 21, 8, 0, 9, 1, 2, 45, 1, 76, 89, 65, 43]

#tomamos como referencia el numero inicial de la lista
max_num = lista[0]

for i in lista:
    if i > max_num:
        max_num = i

print(f"El numero mayor encontrado fue: {max_num}")