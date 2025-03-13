# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos #".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
# - EXTRA: ¿Eres capaz de dibujar más figuras?

filas = int(input("Ingrese la cantidad de filas = "))
print("Siguiente triangulo")

for i in range (0, filas):
    for j in range (0, i+1):
        print("*", end='')
    print()