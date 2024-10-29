'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 24 de Octubre de 2024
Descripción: Ciclo while de 1 hasta n
'''

print("*** Imprimir números hasta el número ingresado en consola ***")

num = int(input("Ingrese un número: "))  #Se solicita un número entero al usuario
i = 1  #Se inicializa el contador en 1

print(f"Los números del 1 al {num} ingresados por el usuario son: ")
while i <= num:  #Un ciclo de 1 hasta n
    print(i, end=" ")  #Se imprime el número y se deja un espacio entre ellos.
    i = i + 1  #Se incrementa el contador de 1 en 1.
print()
print("Fin de la impresión")  #Comentario que indica que terminó el ciclo

print()
print("*** Imprimir números pares hasta el número ingresado en consola ***")

num = int(input("Ingrese un número: "))  #Se solicita otro número entero al usuario
i = 0  #Se inicializa el contador en 0
print(f"Los números pares del 0 al {num} ingresados por el usuario son: ")
while i <= num:  #Un ciclo de 0 hasta n
    print(i, end=" ")  #Se imprime el número par y se deja un espacio entre ellos.
    i = i + 2  #Se incrementa el contador de 2 en 2.
print()
print("Fin de la impresión")  #Comentario que indica que terminó el ciclo
