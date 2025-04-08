"""
Crea una funcion que permita multiplicar dos numeros, sin ocupar el operador * y controlando los 0 y negativos.
"""

def multiplicar(a, b):
    
    isPositivo = abs(b) == b
    res = 0

    if b == 0:
        return 0
    
    for v in range(abs(b)):
        res = res + a if isPositivo else res - a

    return f' {a} x {b} = {res}'

print(multiplicar(5, 8)) #40
print(multiplicar(-9, -8)) #72
print(multiplicar(5, -5)) #-25