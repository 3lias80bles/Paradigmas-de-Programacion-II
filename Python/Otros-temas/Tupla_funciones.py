'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de noviembre de 2024
Descripción:
'''


def promedio_final_funcion(c1, c2, c3, o):
    pp = (c1 + c2 + c3) / 3
    final = (pp + o) / 2
    return pp, final

# codigo a nivel de módulo
parcial1 = float(input("Ingrese su calificacion del parcial 1: "))
parcial2 = float(input("Ingrese su calificacion del parcial 2: "))
parcial3 = float(input("Ingrese su calificacion del parcial 3: "))
ordinario = float(input("Ingrese su calificacion del parcial ordinario: "))

promedio_parcial,promedio_final=promedio_final_funcion(parcial1,parcial2,parcial3,ordinario)

print(f"Tu promedio parcial es {promedio_parcial:.2} y tu promedio final es {promedio_final:.3}")