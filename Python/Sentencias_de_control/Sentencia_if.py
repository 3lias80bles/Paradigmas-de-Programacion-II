'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 23 de octubre de 2024
Descripción:
Este programa utiliza una sentencia de control `if` para determinar si una persona es mayor de edad.
'''

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que debe estar indentado con un tabulador.

# Código que continúa ejecutándose. Notar que ya no hay espacio y está a la misma altura que el if.
"""

print("  ***  Programa que determina si eres mayor de edad  ***")
edad = int(input("Ingrese su edad actual: "))  #Se pide un dato desde consola de tipo entero.

if edad >= 18:  #Verifica si la persona es mayor de edad.
    print("Eres mayor de edad")  #Imprime si cumple la condición siempre debe está indentado con un tabulador.

print("Código de ejemplo")  #Este se ejecuta después del if o directamente si la condición no se cumple.
