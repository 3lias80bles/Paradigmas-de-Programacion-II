'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: Este programa determina si te permiten el acceso al bar "La Negra", considerando la edad y el dinero disponible.
'''

print("*** Bienvenido al bar *La Negra* ***")

#Se solicita la edad y el presupuesto al usuario
edad = int(input("Ingresa tu edad: "))
cantidad = int(input("Ingresa tu presupuesto: "))

#Se verifica las condiciones de acceso al bar
if edad >= 18 and cantidad >= 250:
    print()
    print("¡Bienvenido a tu mejor bar!")
else:#Si no se cumple se imprime lo siguiente
    print()
    print("Lo sentimos, ya estamos por cerrar.")
