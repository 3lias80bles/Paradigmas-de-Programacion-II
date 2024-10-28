'''
Nombre: Sergio Elias Robles Ignacio
Fecha:17 de Octubre de 2024
Descripción:
Este programa realiza diversas operaciones aritméticas utilizando operadores compuestos.
'''

num1 = float(input("Ingrese el primer número: "))  # Solicita el primer número al usuario y lo convierte a tipo float.
num2 = float(input("Ingrese el segundo número: "))  # Solicita el segundo número al usuario y lo convierte a tipo float.

# Suma 4 al valor de num1.
num1 += 4
print(num1)  # Muestra el nuevo valor de num1.

# Resta 6 al valor de num2.
num2 -= 6
print(num2)  # Muestra el nuevo valor de num2.

# Multiplica el valor actual de num1 por 21.
num1 *= 21
print(num1)  # Muestra el nuevo valor de num1.

# Divide el valor actual de num2 entre 11.
num2 /= 11
print(num2)  # Muestra el nuevo valor de num2.

# Calcula el residuo de la división del valor actual de num1 entre 14.
num1 %= 14
print(num1)  # Muestra el residuo obtenido.

# Eleva el valor actual de num2 al cuadrado.
num2 **= 2
print(num2)  # Muestra el nuevo valor de num2.

# Divide el valor actual de num2 entre 3 y toma la parte entera del resultado.
num2 //= 3
print(num2)  # Muestra el resultado de la división entera de num2 entre 3.
