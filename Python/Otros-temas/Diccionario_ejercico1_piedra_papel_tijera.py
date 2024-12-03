'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 19 de noviembre de 2024
Descripción: Implementación del juego de piedra, papel o tijera sin usar random.choice() ni un diccionario para opciones.
'''

import random  # Se importa la librería random para números aleatorios.

# Diccionario para determinar el resultado basado en las opciones.
reglas = {
    "Piedra": {"Piedra": "Empate", "Papel": "CPU", "Tijera": "Jugador"},
    "Papel": {"Piedra": "Jugador", "Papel": "Empate", "Tijera": "CPU"},
    "Tijera": {"Piedra": "CPU", "Papel": "Jugador", "Tijera": "Empate"}
}

# Inicialización de variables.
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Bucle para el menú principal del juego.
while True:
    print()
    print("*** Juego de piedra,papel o tijera ***")
    # Se muestra las estadisticas del juego
    print(f"Victorias del jugador {victorias_jugador}, empates: {empates} y victorias de la CPU: {victorias_cpu}.")
    print("Piedra...........[1]")
    print("Papel............[2]")
    print("Tijeras..........[3]")
    print("Salir............[0]")
    print()

    # Se solicita una opción al usuario.
    opcion = int(input("Su opción es: "))
    if opcion == 0:
        print("Fin del juego...")
        break
    elif opcion < 0 or opcion > 3:  # Verifica que la opción sea válida.
        print("Opción no válida. Intente nuevamente.")
        continue

    # Convierte la opción del jugador a texto.
    if opcion == 1:
        opcion_jugador = "Piedra"
    elif opcion == 2:
        opcion_jugador = "Papel"
    else:
        opcion_jugador = "Tijera"

    # Genera una opción aleatoria para la CPU.
    opcion_CPU_numero = random.randint(1, 3)
    if opcion_CPU_numero == 1:
        opcion_CPU = "Piedra"
    elif opcion_CPU_numero == 2:
        opcion_CPU = "Papel"
    else:
        opcion_CPU = "Tijera"

    # Determina el resultado del juego.
    resultado = reglas[opcion_jugador][opcion_CPU]
    if resultado == "Empate":
        empates += 1
    elif resultado == "Jugador":
        victorias_jugador += 1
    else:
        victorias_cpu += 1

    # Imprime el resultado del juego.
    print(f"Jugador: {opcion_jugador}, CPU: {opcion_CPU}. Resultado: {resultado}.")