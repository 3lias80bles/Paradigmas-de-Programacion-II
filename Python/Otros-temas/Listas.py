'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 11 de noviembre de 2024
Descripción: En este programa se utiliza el ciclo for
'''
#ordenados
# mutables
#[0]      [1]   [2]   [3]    [4]    [5]
#Amelia albert Kevin Elton Magdiel Diana

alumnos = ["Amelia","Albert"]

print(f"Alumnos de la lista: {alumnos}")

alumnos.append("Kevin")#Añade un elemento al dinal de la lista

alumnos.append("Diana")#Añade un elemento en un índice especifico
alumnos.insert(3,"Elton")

alumnos.insert(4,"Magdiel")

alumnos.append("Eden")
alumnos.append("Sergio")

alumnos.insert(7,"Magdiel")
alumnos.append("Magdiel")

#Borra un elemento por su valor
alumnos.remove("Magdiel")

#Borrar por su índice
alumnos.pop(6)
#otra manera
del alumnos [7]

alumnos.len()
alumnos.sort()
alumnos.sort(reserve=true)

print(f"{alumnos}")
