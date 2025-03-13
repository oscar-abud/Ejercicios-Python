# Crear una funcion que detecte en una lista de numeros el mas repetido.

def mas_repetido(numeros):

    lista = {} #Lista vacia

    for num in numeros: #Iteramos en numeros
        if num in lista: #Preguntamos si numero esta en la lista
            lista[num] += 1 #De ser verdad, a la llave correspondiente se le sumara su valor en 1
        else:
            lista[num] = 1 #De lo contrario, se le otorgara un valor por defecto empezando en 1

    num_rep = 0 #Variable que nos servira para mostrar el numero repetido mayor
    rep_veces = 0 #Variable que nos servira para mostrar cuantas veces se repite el numero

    for num, rep in lista.items(): #Iteramos tanto la llave (numero) y su valor (veces repetido), en la lista
        if rep > rep_veces: #Preguntamos si el valor de la llave es mayor a 0
            num_rep = num #De ser verdad, la variable sera reemplazada por la llave
            rep_veces = rep #La variable sera reemplazada por el valor de la llave

    print(f"El numero {num_rep} se repite {rep_veces}") #Y luego mostramos esas variables en un print


lista_numeros = [1, 1, 1, 4, 5, 6, 4, 3, 4, 7, 6, 5, 8, 9, 1, 7, 8, 3, 6, 6, 5, 7, 8, 8, 3]

mas_repetido(lista_numeros)