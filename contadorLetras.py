"""
Te han dado un texto largo. El objetivo es contar cuántas palabras únicas aparecen en el texto, sin tener en cuenta mayúsculas, minúsculas ni repeticiones. Al final, debes devolver un diccionario donde la clave sea la palabra, y el valor sea el número de veces que aparece.

✅ Reglas:
Ignora la puntuación (coma, punto, etc.) en las palabras.

No te importan las mayúsculas ni las minúsculas (por ejemplo, Hola y hola cuentan como la misma palabra).

Devuelve un diccionario con las palabras únicas y su cantidad de veces que aparecen en el texto.
"""

import string

def contadorLetras(texto):

    texto = texto.lower()
    texto = ''.join([char for char in texto if char in string.ascii_letters or char.isspace()])

    lista_texto = texto.split()
    dictString = {}

    for i in lista_texto:
        if i in dictString:
            dictString[i] += 1
        else:
            dictString[i] = 1
    return dictString if dictString else 'No hay palabras'

mensaje = "Hola, hola, ¿cómo estás? Estoy bien. ¿Y tú?"
print(contadorLetras(mensaje))