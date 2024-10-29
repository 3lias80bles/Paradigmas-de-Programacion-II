'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 23 de Octubre de 2024
Descripción: Ejercicio para ver el funcionaiento del if_else.
'''

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

print("*** Número par o impar ***")
num = int(input("Ingrese un número: "))  #Se pide un dato entero.

if num % 2 == 0:  #Se realiza el módulo 2 y si es 0 (par) entra en la condición.
    print("El número es par")
else:  #En caso de no ser par, pasa al else e imprime lo siguiente.
    print("El número no es par")  #La tabulación es importante.
