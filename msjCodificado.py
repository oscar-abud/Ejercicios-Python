"""
Unos alienígenas enviaron un mensaje secreto en forma de números. Cada número representa la posición de una letra en el abecedario.

Por ejemplo:
Mensaje: [8, 5, 12, 12, 15]
Significado: 'hello'
(Porque 8 = 'h', 5 = 'e', 12 = 'l', etc.)

Tu misión es escribir una función que reciba una lista de números y devuelva el mensaje original.

✅ Reglas:
Las letras van de 1 a 26 (a a z).

Ignora cualquier número que no esté entre 1 y 26.

Si quieres hacerlo más cool: permite también códigos como '27' para representar un espacio.
"""

def msjCodificado(lista):
    
    num_to_letra = {
        1: 'a',  2: 'b',  3: 'c',  4: 'd',  5: 'e',
        6: 'f',  7: 'g',  8: 'h',  9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
        16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
        26: 'z', 27: ' '
    }   

    resultado = ''

    for numero in lista:
        if  1 <= numero <= 27:
            resultado += num_to_letra[numero]
    
    return resultado if resultado else 'No hay mensaje'

# Ejemplo de uso
mensaje = [8, 5, 12, 12, 15]
print(msjCodificado(mensaje))  # Salida: 'hello'

mensaje2 = [8, 5, 12, 12, 15, 27, 23, 15, 18, 12, 4]
print(msjCodificado(mensaje2))  # Salida: 'hello world'

print(msjCodificado(mensaje))  # Salida: 'hello'