##Ingresa una palabra y si contiene alguna vocal, deberia mostrar la cantidad de vocales

vocales = "aeiouAEIOU"

string = input("Ingrese una plabra: ")

contador = 0

for i in string:
    if i in vocales:
        contador+= 1

print(f"La palabra {string} tiene {contador} vocales.")