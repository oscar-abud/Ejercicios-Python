# Crea una función que transforme grados Celsius en Fahrenheit
# y viceversa.
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#   y su unidad ("C" o "F").
# - En caso contrario retornará un error.
# Formula matematica (0 °C × 9/5) + 32 = 32 °F
#Me falta por terminar, agregarle el metodo round(), para que en caso de que retorne un resultado con decimales, no muestre más allá de 2 decimas despues de la coma.

def conversor_GradosC(gradosF):
    gradosC = (gradosF - 32) * 5/9
    print("-"*20)
    print(f"Los grados {gradosF} °F serian {gradosC} C°")

def conversor_GradosF(gradosC):
    gradosF = (gradosC * 9/5) + 32
    print("-"*20)
    print(f"Los grados {gradosC} C° serian {gradosF} °F")

print("Bienvenido!")

opcion = input("Quiere ejecutar el menu?: ").lower()

while opcion == "si" and opcion != "no":
    print("-"*20)
    print("Escoga las siguisguientes opciones \n 1.Convertor de grados F° a C° \n 2.Convertor de grados C° a F° \n 3.Terminar el programa")
    opcionMenu = int(input("Ingrese la opcion: "))
    print("-"*20)
    match opcionMenu:

        case 1:
            gradosF = (input("Ingrese el grado F° para convertirlo a C°: "))
            if gradosF.endswith("°F") == True:
                gradosF = gradosF.replace("°F", "")
                grados = int(gradosF)
                conversor_GradosC(grados)
            else:
                print("-"*20)
                print("Error, ingrese un valor correcto (además del número, ingrese tambíen el '°' y 'F')")
                
        case 2:
            gradosC = (input("Ingrese el grado C° para convertirlo a F°: "))
            if gradosC.endswith("°C") == True:
                gradosC = gradosC.replace("°C", "")
                Grados = int(gradosC)
                conversor_GradosF(Grados)
            else:
                print("-"*20)
                print("Error, ingrese un valor correcto (además del número, ingrese tambíen el '°' y 'C')")

        case 3:
            opcion = "no"
            break

        case _:
            print("Escoga una opcion válida")

print("Hasta pronto :)")