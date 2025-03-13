# Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#   estén presentes en str1.

def eliminarCaracter(string1, string2):
    out1 = ""
    out2 = ""
    for i in string1.lower():
        if i not in string2.lower():
            out1 = out1 + i
    for j in string2.lower():
        if j not in string1.lower():
            out2 = out2 + j
    print(f"Entre las palabras '{string1}' y '{string2}' las letras que no son iguales son '{out1}' y '{out2}'")


cadena1 = input("Ingresa el primer caracter: ")
cadena2 = input("Ingresa el segundo caracter: ")

eliminarCaracter(cadena1, cadena2)