'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de noviembre de 2024
Descripción:Ejemplos del uso de una tupla dentro de una función.
'''

def promedio_final_funcion(cal1, cal2, cal3, ord):
    prom_par = (cal1 + cal2 + cal3) / 3
    final = (prom_par + ord) / 2
    return prom_par, final

#Codigo a nivel de módulo
parcial1 = float(input("Ingrese su calificacion del parcial 1: "))
parcial2 = float(input("Ingrese su calificacion del parcial 2: "))
parcial3 = float(input("Ingrese su calificacion del parcial 3: "))
ordinario = float(input("Ingrese su calificacion del parcial ordinario: "))

#Se almacenan los 2 promedios desde la función que realizó las operaciones.
promedio_parcial,promedio_final=promedio_final_funcion(parcial1,parcial2,parcial3,ordinario)

#Imprime el promedio parcial y final.
print(f"Tu promedio parcial es {promedio_parcial:.2} y tu promedio final es {promedio_final:.3}")
