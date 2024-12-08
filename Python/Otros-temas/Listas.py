'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 11 de noviembre de 2024
Descripción: En este programa se utilizan las listas
'''
#ordenados
# mutables
#[0]      [1]   [2]   [3]    [4]    [5]
#Amelia albert Kevin Elton Magdiel Diana

#Lista de alumnos inicial
alumnos = ["Amelia", "Albert"]

print(f"Alumnos de la lista: {alumnos}")

alumnos.append("Kevin")  #Se añade un elemento al final de la lista
alumnos.append("Diana")

#Añade un elemento en un índice especifico
alumnos.insert(3, "Elton")
alumnos.insert(4, "Magdiel")

# Añadiendo más elementos al final de la lista
alumnos.append("Eden")
alumnos.append("Sergio")

# Inserta nuevamente a 'Magdiel' en la posición 7
alumnos.insert(7, "Magdiel")
alumnos.append("Magdiel")

#Borra un elemento por su valor
alumnos.remove("Magdiel")

#Borrar un elemento por su índice
alumnos.pop(6)  # Elimina el elemento en el índice 6
del alumnos[7]  # Otra manera de eliminar un elemento por su índice

#Verifica la longitud de la lista
len(alumnos)

# Ordena la lista alfabéticamente
alumnos.sort()
alumnos.sort(reverse=True)

print(f"Alumnos después de las modificaciones: {alumnos}")