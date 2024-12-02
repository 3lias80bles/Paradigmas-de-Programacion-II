'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 29 de Octubre de 2024
Descripción: En este programa se utiliza el ciclo for
'''

espacio=" "
asterisco= "*"
n=4
i=1

print()
print("Piramide 1")
for i in range (1,n+1):
    espacios = espacio * (n - i)
    asteriscos = asterisco * i
    print(f"{asteriscos}{espacios}")
print()
print("piramide 2")
for i in range (1,n+1):
    asteriscos = asterisco * ((n-i)+1)
    espacios = espacio * i
    print(f"{asteriscos}{espacios}")
print()
print("Piramide 3")
for i in range(1, n + 1):
    espacios = espacio * (n - i)
    asteriscos = asterisco * (2 * i - 1)
    print(f"{espacios}{asteriscos}")

print()
print("Piramide 4")
for i in range (1,n+1):
    espacios = espacio * (n - i)
    asteriscos = asterisco * i
    print(f"{espacios}{asteriscos}")

print()
print("piramide Extra")
for i in range (1,n+1):
    asteriscos = asterisco * ((n-i)+1)
    espacios = espacio * (i-1)
    print(f"{espacios}{asteriscos}")



