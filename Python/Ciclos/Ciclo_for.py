'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 29 de Octubre de 2024
Descripción: En este programa se utiliza el ciclo for.
'''

print("*** Ejemplo de ciclo for ***")

#Se solicita al usuario que ingrese una cadena
cadena = input("Ingrese una cadena: ")

#Se recorre cada carácter de la cadena ingresada por el usuario
for caracter in cadena:  #Podemos decir que 'caracter' toma el valor de cada elemento, uno por uno
    print(caracter, end="-")  #Imprime cada carácter separado por un guion
print()  #Salto de línea al finalizar el ciclo
print("Fin de la cadena")

#Se define una lista de nombres
alumnos = ["Albert", "Kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio"]

#Se recorre cada nombre en la lista
for alumno in alumnos:
    print("Hola", alumno)  #Imprime "Hola" seguido del nombre de cada alumno
print("Fin de la cadena")