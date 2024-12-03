'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 29 de Octubre de 2024
Descripción: En este programa se utiliza el ciclo for
'''

#Se definene las variables de espacios y asteriscos
espacio=" "
asterisco= "*"
i=1

#Se pide el tamaño del la piramide con un numero desde el teclado
tama = int(input("Ingresa el número de filas de la piramide: "))
print()

# Pirámide 1: Crece hacia la izquierda
print("*** Piramide 1 ***")
for i in range (1,tama+1): #Itera desde 1 hasta el número de filas
    espacios = espacio * (tama - i) #Decrementa los espacios en cada fila empezando del tamaño menos 1
    asteriscos = asterisco * i #Incrementa los asteriscos en cada fila
    print(f"{asteriscos}{espacios}") #Imprime los asteriscos seguidos de espacios
print()

# Pirámide 1: Crece hacia la izquierda
print("*** Piramide 2 ***")
print()
for i in range (1,tama+1): #Itera desde 1 hasta el número de filas
    asteriscos = asterisco * ((tama-i)+1) #Decrementa los asteriscos
    espacios = espacio * i #aumenta los espacios
    print(f"{asteriscos}{espacios}")#Imprime los asteriscos seguidos de espacios
print()

# Pirámide 1: Crece hacia la izquierda
print("*** Piramide 3 ***") #Itera desde 1 hasta el número de filas.
print()
for i in range(1, tama + 1): #Itera desde 1 hasta el número de filas.
    espacios = espacio * (tama - i) #Calcula los espacios para centrar la pirámide.
    asteriscos = asterisco * (2 * i - 1) #Incrementa los asteriscos de forma impar.
    print(f"{espacios}{asteriscos}")#Imprime los espacios seguidos de asteriscos.

print()

# Pirámide 1: Crece hacia la izquierda
print("*** Piramide 4 ***")#Itera desde 1 hasta el número de filas
print()
for i in range (1,tama+1): #Itera desde 1 hasta el número de filas.
    espacios = espacio * (tama - i) #Calcula los espacios para centrar la pirámide.
    asteriscos = asterisco * i #Aumenta los asteriscos
    print(f"{espacios}{asteriscos}") #Imprime los espacios seguidos de asteriscos.
print()

# Pirámide 1: Crece hacia la izquierda
print("*** Piramide Extra ***")#Itera desde 1 hasta el número de filas
print()
for i in range (1,tama+1):
    asteriscos = asterisco * ((tama-i)+1)
    espacios = espacio * (i-1)
    print(f"{espacios}{asteriscos}")



