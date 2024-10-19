'''
Nombre: Sergio Elias Robles Ignacio
Fecha:18 de Octubre de 2024
Descripción:
'''

si_no=input("Ingresa Si o No: ")
si_no = si_no.lower() == "si"
print(f"El resultado en boleano es: {si_no}")
print()
no_si=input("Ingresa Si o No: ")
no_si = no_si.lower() == "si"
print()
print(f"El resultado en boleano es: {si_no}")
print()
print(f"Los dos valores que ingresaste son iguales? {si_no and no_si}")
print()
print(f"Los dos valores que ingresaste son diferentes? {si_no or no_si}")
print()
print(f"La negación del primero valor es: {not si_no}")
print()
print(f"La negación del segundo valor es: {not no_si}")

