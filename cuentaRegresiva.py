#Crea una funcion que reciba dos parametros para crear una cuenta atras.
# - El primero, representa el numero en el que comienza la cuenta.
# - El segundo, los que tienen que transcurrir entre cada cuenta.
# - Solo se aceptan numeros enteros positivos.
# - El programa finaliza al llegar a cero.
# - Debes imprimir cada numero de la cuenta atras.

def cuentaRegresiva(inicio, tiempo):
    while inicio >= 0:
        print(f"cuenta regresiva: {inicio}")
        inicio = inicio - tiempo
    print("El programa ha finalizado")

ini = int(input("Ingrese el tiempo del contador: "))
tie = int(input("Ingrese el numero que ira de paso a paso disminuyendo el tiempo: "))

cuentaRegresiva(ini, tie)