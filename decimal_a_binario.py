# Crea un programa se encargue de transformar un número decimal
# a binario sin utilizar funciones propias del lenguaje que
# lo hagan directamente.

# Calculando un numero decimal a binario ej => 34 : 2 = 17 (sobran 0 decimales) => 17 : 2 = 8 (sobra 1 decimal) => 8 : 2 = 4 (sobran 0 decimales) => 4 : 2 = 2 (sobran 0 decimales) 2 : 2 = 1 (sobran 0 decimales) 1 : 2 = 0 (sobra 1 decimal) entonces los numeros binarios serian 100010

def calcularBinario(num):
    if num == 0:
        print("El numero decimal 0 a binaria seria 0")
        return #El return hace que la funcion finalice
    
    variable = []
    n = num  # Guardamos el valor original para el mensaje final
    while num > 0:
        variable.append(num % 2)
        num = num // 2  # Actualizamos num para la siguiente iteración (// es para dividir redondeando el resultado, para no dejar decimales)
    
    variable.reverse()  # El orden de los bits está invertido
    print(f"El numero decimal {n} a binaria seria: ", end='')
    for i in variable:
        print(f"{i}", end='')
    

numero = int(input("Ingrese un numero: "))
calcularBinario(numero)