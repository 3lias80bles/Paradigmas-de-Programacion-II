'''
Nombre: Sergio Elias Robles Ignacio
Fecha:18 de Octubre de 2024
Descripción: En este trabajo se realizan operaciones lógicas básicas con los valores ingresados.
'''

print("*** Operaciones logicas ***")
#Se pide un dato de tipo String al usuario
si_no = input("Ingresa Si o No: ")
si_no = si_no.lower() == "si"  #Convierte la cadena a minúsculas y compara si es igual a "si"
print(f"El resultado en booleano es: {si_no}")  #Muestra si el resultado es True o False

print()
# Se repite el proceso anterior
no_si = input("Ingresa Si o No: ")
no_si = no_si.lower() == "si"
print(f"El resultado en booleano es: {no_si}")  #Muestra si el resultado es True o False

print()  # Salto de línea

#Se usan los operadores lógicos básicos: "and", "or" y "not".
print(f"¿Los dos valores que ingresaste son iguales? {si_no and no_si}")  # "and" verifica si ambos valores son verdaderos

print()
print(f"¿Al menos uno de los valores que ingresaste es verdadero? {si_no or no_si}")  # "or" verifica si al menos uno es verdadero

print()
print(f"La negación del primer valor es: {not si_no}")  # "not" invierte el valor booleano del primer valor

print()
print(f"La negación del segundo valor es: {not no_si}")  # "not" invierte el valor booleano del segundo valor

