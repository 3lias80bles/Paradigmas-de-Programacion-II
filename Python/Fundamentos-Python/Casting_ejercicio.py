'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 octubre de 2023
Descripción:
Conversión de tipos de datos (casting) en Python ejercicio.
'''

# *****   Conversión de número a cadena     *****
var_cero = 0  # Declaración de variables
var_int = 12
var_float = 3.14159265

print()
print("Conversión de número a cadena.")
print(f"Los números {var_int}, {var_float} y {var_cero} se convierten a cadena utilizando str(var_int): {str(var_int)}, "
      f"str(var_float): {str(var_float)}, y str(var_cero): {str(var_cero)}")
print()

# *****   Conversión a booleano     *****
var_cero = 0
var_int = 12
var_float = 3.14159265

print("Conversión a booleano:")
print(f"¿El valor de {var_cero} es verdadero? {bool(var_cero)}.")  # Esto nos da False
print(f"¿El valor de {var_int} es verdadero? {bool(var_int)}.")  # Esto nos da True
print(f"¿El valor de {var_float} es verdadero? {bool(var_float)}.")  # Esto nos da True
print()

# *****   Conversión de cadena a entero     *****
var_cadena = "10002"
var_float = "100.02"
var_cero = "0"
var_int = int(var_cadena)
var_flo = float(var_float)  # No se puede convertir a entero pero sí a flotante.
var_int2 = int(var_cero)

print("Conversión de cadena a entero.")#Se imprimen los resultados
print(f"Número como cadena: {var_cadena}.")
print(f"Número como int: {var_int}.")
print()
print(f"Número como cadena: {var_float}.")
print(f"Número como float: {var_flo}.")
print()
print(f"Número como cadena: {var_cero}.")
print(f"Número como int: {var_int2}.")
print()

# *****   Conversión a booleano de enteros y flotantes *****

print("Conversión a booleano de enteros y flotantes:")
print(f"¿El valor de {var_int} es verdadero? {bool(var_int)}.")  # Esto nos da True
print(f"¿El valor de {var_flo} es verdadero? {bool(var_flo)}.")  # Esto nos da True
print(f"¿El valor de '{var_cero}' es verdadero? {bool(var_cero)}.")  # True, porque la cadena no está vacía
print()
