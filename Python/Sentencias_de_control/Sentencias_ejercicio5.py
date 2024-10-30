'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: Este programa determina si el estudiante pasa el semestre de manera aprobatoria, considerando las calificaciones parciales y ordinarias.
'''

print("*** Programa para calcular el promedio de una materia ***")
#Se piden las calificaciones de los parciales y del ordinario como números flotantes
parcial1 = float(input("Ingresa la calificación del parcial 1: "))
parcial2 = float(input("Ingresa la calificación del parcial 2: "))
parcial3 = float(input("Ingresa la calificación del parcial 3: "))
ordinario = float(input("Ingresa la calificación del ordinario: "))

#Se calcula el promedio de los tres parciales y del ordinario
promedio = (((parcial1 + parcial2 + parcial3) / 3) + ordinario) / 2

#Se verifica si el promedio es mayor o igual a 6 para aprobar
if promedio >= 6:
    print()
    print(f"La calificación final es de {promedio:.2f}. ¡Felicidades! Aprobaste.")  #Mensaje de aprobación.
else:
    print()
    print(f"La calificación final es de {promedio:.2f}. Lo siento, no aprobaste.")  #Mensaje de reprobación ):.
