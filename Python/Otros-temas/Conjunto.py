'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de noviembre de 2024
Descripción: ejercicio donde se muestran diferentes tipos de conjuntos.
'''

# Conjuntos:
# Características:
# - Desordenados: Los elementos no tienen un orden específico.
# - Mutables: Se pueden añadir o eliminar elementos.
# - Representación:
#   - Listas: []
#   - Tuplas: ()
#   - Conjuntos: {}
#   - Conjunto vacío: set()

# Creación de un conjunto vacío
conjunto1 = set()

# Creación de un conjunto con valores predefinidos
conjunto2 = {10, 5, 24, 11, 8, 7, 21, 9}
print(conjunto2)

# Añadiendo elementos al conjunto1
conjunto1.add(80)  # Añade 80 al conjunto
conjunto1.add(111)  # Añade 111 al conjunto
conjunto1.add(10)  # Añade 10 al conjunto
conjunto1.add(24)  # Añade 24 al conjunto
conjunto1.add(80)  # No añade 80 nuevamente porque ya existe (los conjuntos no permiten duplicados)
print(conjunto1)
print()

# Eliminando elementos del conjunto1
conjunto1.remove(111)  # Elimina 111 del conjunto
# conjunto1.remove(111)  # Generaría un error porque 111 ya no existe en el conjunto
conjunto1.discard(111)  # No genera error si el elemento no existe
conjunto1.discard(10)  # Elimina 10 del conjunto
print(conjunto1)

# Operaciones entre conjuntos

# Unión: Combina todos los elementos de ambos conjuntos
conjunto_union = conjunto1 | conjunto2
print(conjunto_union)

# Intersección: Obtiene los elementos comunes entre ambos conjuntos
conjunto_interseccion = conjunto1 & conjunto2
print(conjunto_interseccion)

# Diferencia: Obtiene los elementos que están en conjunto1 pero no en conjunto2
resta_conjuntos = conjunto1 - conjunto2
print(resta_conjuntos)

# Lista de alumnos
alumnos_lista = ["albert", "kevin", "Elton", "Diana", "Rosendo", "Amelia", "Sergio"]

# Añadiendo un elemento duplicado a la lista
alumnos_lista.append("Elton")  # Aunque se permite en listas, los conjuntos lo gestionarán después
print(alumnos_lista)

# Convertir la lista en un conjunto para eliminar duplicados
alumnos_conjnto = set(alumnos_lista)
print(alumnos_conjnto)

# Entrada del usuario
nombre = input("Ingrese un nombre: ")  # Solicita un nombre al usuario
nombre = nombre.strip()  # Elimina espacios en blanco al principio y final

# Verifica si el nombre está en el conjunto
if nombre in alumnos_conjnto:
    print("Se encuentra en el conjunto.")  # Mensaje si el nombre ya está en el conjunto
else:
    print("Se añadió al conjunto: ")  # Mensaje si el nombre no está en el conjunto
alumnos_conjnto.add(nombre)  # Añade el nombre al conjunto
