# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

aux = []
texto = ""

string = input("Ingrese la palabra que quiere invertir sus letras: ")

for i in string:
    aux.insert(0, i) #Guardamos las palabras en el indice 0
for j in aux:
    texto = texto + j #Iteramos la lista y lo guardamos en forma de caracter en una variable que no es un array, para que se vea mas bonito y presentable el resultado

print(f"El texto '{string}' invertido es '{texto}'")