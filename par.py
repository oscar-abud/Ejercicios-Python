#Cree un programa que detecte si el numero es par o impar y que lo mestre en pantalla
# - Cabe recalcar que el numero debe ser positivo y entero

num = int(input("Ingrese el numero maximo => "))

for i in range (0, num+1):
    if i % 2 == 0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")
