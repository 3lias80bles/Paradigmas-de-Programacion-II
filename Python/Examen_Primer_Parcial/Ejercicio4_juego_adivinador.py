'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se realiza un juego de para adivinar de un número aleatorio.
'''

import random #Se importa la libreria random patra números aleatoreos.

#Inicialización de variables.
num_intento = 1  # Contador de intentos
num_adivinar = random.randint(1, 100)  #Se genera el número a adivinar antes del bucle
#print(f"{num_adivinar}")

#Bucle para el juego, solo tenemos 5 intentos
while num_intento <= 5:
    print()
    print("*** Juego del adivinador ***")
    #Se solicita un número y marca el número de intentos
    numero = int(input(f"Número de intento {num_intento}. Ingresa un número (1-100): "))

    # Verifica si el número ingresado es menor, mayor o igual al número a adivinar
    if numero < num_adivinar:
        print("El número a adivinar es mayor.")
    elif numero > num_adivinar:
        print("El número a adivinar es menor.")
    else:
        print(f"Feliceidades, Adivinaste en {num_intento} intentos.")
        break  #Se rompe el bucle  al entrar en el else.

    num_intento += 1  #Se incrementa el contador

#Si el contador pasa de los 5 intentos imprime lo siguiente
if num_intento > 5:
    print(f"Perdiste. El número era {num_adivinar}.")
