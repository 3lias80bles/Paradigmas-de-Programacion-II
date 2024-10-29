'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 23 de Octubre de 2024
Descripción: Ejercicio para ver el funcionamiento del if_elif_else
'''
print("*** Programa que determina la estación del año de acuerdo al mes ***")
mes = int(input("Ingrese el número de su mes actual (1-12): "))  #Se pide un dato entero.

estacion = ""  #Se agrega una cadena vacía.

if mes == 12 or 1 <= mes < 3:  #Si el mes es 12, 1 o 2.
    estacion = "Invierno"
elif 3 <= mes < 6:  #Entonces, si es mayor o igual a 3 y menor a 6 se realiza:
    estacion = "Primavera"
elif 6 <= mes < 9:  #Entonces, si es mayor o igual a 6 y menor a 9 se realiza:
    estacion = "Verano"
elif 9 <= mes < 12:  #Entonces, si es mayor o igual a 9 y menor a 12 se realiza:
    estacion = "Otoño"
else:  #Si no, entonces:
    estacion = "Mes incorrecto"

print()
#Imprime la estación correspondiente.
print(f"La estación es: {estacion}")
