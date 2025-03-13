# Contador de palabras
# Pedir al usuario una frase y contar cuantas palabras tiene

palabra = input("Ingresa la frase: ")
valor = 0

for i in range (len(palabra)):
    valor = i
    
print(f"La palabra {palabra} tiene {valor+1} palabras")
