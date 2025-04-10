"""
    Dada una lista de números enteros y un número target, determina los índices de los dos números en la lista que suman el número target.
    Por ejemplo, si la lista es [2, 7, 11, 15] y el target es 9, la función debe devolver [0, 1] porque nums[0] + nums[1] es igual a 9.
    Si no hay solución, la función debe devolver un array vacío.
"""

lista = [2, 7, 11, 15, 5, 1, 4]

target = 11

#Salida esperada: [1, 6]

def sumaIndices(array, target):
    
    for i in array:
        if i < target:
            for j in array:
                if j < target and i + j == target: #Python lee de izquierda a derecha, asi que si la condicion de la izquierda no se cumple, la de la derecha no se ejecuta.
                    return f"De la lista {array} \n{i} + {j} = {target}, \nlos indices de la suma: {array.index(i)} y {array.index(j)}"
    return "No hay solución"

print(sumaIndices(lista, target))