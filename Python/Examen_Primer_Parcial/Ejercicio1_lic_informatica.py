'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 25 de Octubre de 2024
Descripción: Este programa imprime en consola los números, separados por comas,
del 1 hasta un número ingresado por el usuario, sin embargo hay unas condiciones que deben cumplir.
'''

print()
print("*** Múltiplos ***")

i = 1 #Inicializa la variable de contador i en 1.

#Se solicita al usuario el número hasta el cual se desea contar.
num_fin = int(input("Ingresa el número final de la cuenta: "))

#Comienza un ciclo que se ejecuta mientras i sea menor o igual al número final.
while i<=num_fin:
    #Si i es múltiplo de 3 y 5, imprime "Licenciatura en informática".
    if i%5 == 0 and i%3 == 0:
        print("Licenciatura en informatica",end= "\n")
    #Si i es múltiplo de 3, imprime "Licenciatura".
    elif i%3 == 0:
        print("Licenciatura",end= ",")
    #Si i es múltiplo de 5, imprime "Informática".
    elif i%5 == 0:
        print("Informatica",end= ",")
    #Si no es múltiplo de 3 ni de 5, imprime el valor de i
    else:
        print(i,end= ",")
    i += 1 #Incrementa el valor de i en 1 al final de cada iteración.
