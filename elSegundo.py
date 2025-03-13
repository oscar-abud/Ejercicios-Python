# Dado un listado de números, encuentra el SEGUNDO más grande

def segundoGrande(lista):
    lista.sort()
    print("-"*10)
    print(f"Números = {lista}")
    lista.reverse()
    print("-"*10)
    print(f"Números ordenados = {lista}")
    print("-"*10)
    print(f"El segundo numero más grande es {lista[1]}")
    print("-"*10)


numeros = []
agregar = int(input("Agregue un numero a la lista: "))
numeros.append(agregar)

opcion = input("Desea agregar otro numero?: ")

while opcion.lower() == "si" and opcion.lower() != "no":
    agregar = int(input("Agregue un numero a la lista: "))
    numeros.append(agregar)
    opcion = input("Desea agregar otro numero?: ")

segundoGrande(numeros)
