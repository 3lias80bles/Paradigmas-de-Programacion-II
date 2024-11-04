'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: En este trabajo se usa la libreria random para realizar el juego de piedra, papel o tijera.
'''

import random #Se importa la libreria random patra números aleatoreos

#Inicialización de variables.
i = 0
opcion = 5
victorias_jugador = 0
victorias_cpu = 0
empates = 0
#Bucle para el menú principal del juego.
while opcion!=0:
    print()
    print("*** Juego de piedra,papel o tijera ***")
    #Se muestra las estadisticas del juego
    print(f"Victorias del jugador {victorias_jugador}, empates: {empates} y victorias de la CPU: {victorias_cpu}.")
    print("Piedra...........[1]")
    print("Papel............[2]")
    print("Tijeras..........[3]")
    print("Salir............[0]")
    print()
    #Se solicitar una opción al usuario.
    opcion=int(input("Su opción es: "))
    #Si la opción es 0 sale del juego.
    if opcion == 0:
        print("Fin del juego...")
        break#Rompe el ciclo para salir del juego y no avanzar.
    #Asigna la opción de número del jugador a texto.
    elif opcion == 1:
        opcion_jugador = "Piedra"
    elif opcion == 2:
        opcion_jugador = "Papel"
    elif opcion == 3:
        opcion_jugador = "Tijera"
    else:#Si la opción ingresada no es correcta.
        print("Opción no valida.")
        continue#es lo contrario al break, continua el programa y como no tenia datos inicia en 0s.

    #Se define la opción que elige la CPU unsando la opción random  y se guarda en una variable.
    opcion_CPU = random.randint(1, 3)
    # Asigna la opción de número del CPU a texto.
    if opcion_CPU == 1:
        opcion_CPU_texto = "Piedra"
    elif opcion_CPU == 2:
        opcion_CPU_texto = "Papel"
    else:
        opcion_CPU_texto = "Tijera"
    #Se define el ganador
    if opcion == opcion_CPU:
        resultado = "El resultado es empate"
        empates += 1
    elif (opcion == 1 and opcion_CPU == 3) or (opcion == 2 and opcion_CPU == 1) or (opcion == 3 and opcion_CPU == 2):
        resultado = "El ganador es el jugador"
        victorias_jugador += 1
    else:
        resultado = "El ganador es la CPU"
        victorias_cpu += 1
    #Se imprime el resultado del juego.
    print(f"Jugador: {opcion_jugador}, CPU: {opcion_CPU_texto}. {resultado}")