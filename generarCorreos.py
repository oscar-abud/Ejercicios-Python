#
# Genera un numero personalizado de correos numerados con tu nombre
# - Ejemplo Oscar1@gmail.com Oscar2@gmail.com

nombre = input("Ingrese su nombre para el correo: ")
veces = int(input("Ingrese la cantidad de correos que quiere generar: "))

print("A continuacion los siguientes correos: \n")
for i in range(1, veces+1):
    print(f"{nombre}{i}@gmail.com")
    print("-"*20)