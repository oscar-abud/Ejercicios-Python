"""
Objetivo: Escribir una función que verifique si una contraseña es fuerte o no.

✅ Reglas para que una contraseña sea fuerte:
Tiene al menos 8 caracteres.

Contiene al menos una letra minúscula.

Contiene al menos una letra mayúscula.

Contiene al menos un número.

Contiene al menos un carácter especial (por ejemplo: !@#$%^&*()-_+=).
"""

def strongPassword(password):

    if password.strip() == '':
        return 'No hay contraseña'
    
    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero    = False
    tiene_simbolo   = False

    if len(password) < 8:
        return 'La contraseña es débil'

    for char in password:
        if char.islower():
            tiene_minuscula = True
        elif char.isupper():
            tiene_mayuscula = True
        elif char.isdigit():
            tiene_numero = True
        elif char in "!@#$%^&*()-_+=<>?":
            tiene_simbolo = True

    return 'La contraseña es fuerte' if tiene_minuscula and tiene_mayuscula and tiene_numero and tiene_simbolo else 'La contraseña es débil'


print(strongPassword('Hola123!'))  # Salida: 'La contraseña es fuerte'
print(strongPassword('Hola123'))   # Salida: 'La contraseña es débil'
print(strongPassword(''))  # Salida: 'La contraseña es débil'
          