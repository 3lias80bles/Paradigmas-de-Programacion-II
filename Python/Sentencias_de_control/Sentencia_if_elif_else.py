'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 23 de Octubre de 2024
Descripción: Ejercicio para ver el funcionamiento del if_elif_else
'''
print("*** Programa que determina el grupo de acuerdo a la edad ***")
edad = int(input("Ingrese su edad actual: "))  # Se pide un dato entero.

if edad < 14:  #Si es menor a 14 entonces:
    print("Eres niño o adolescente.")
elif 15 <= edad < 25:  #Entonces, si es mayor o igual a 15 y menor a 25 se imprime:
    print("Eres joven.")
elif 25 <= edad < 45:  #Entonces, si es mayor o igual a 25 y menor a 45 se imprime:
    print("Eres adulto joven.")
elif 45 <= edad < 60:  #Entonces, si es mayor o igual a 45 y menor a 60 se imprime:
    print("Eres adulto maduro.")
else:  # Si no, entonces:
    print("Eres adulto mayor.")
