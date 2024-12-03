'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 13 de noviembre de 2024
Descripción:
'''


calificaciones_parcial1=(9.6,6.3,6.0,8.7,5.0)

poo,bd,redes,ara,ings=calificaciones_parcial1
print(calificaciones_parcial1)

for calificacion in calificaciones_parcial1:
    print(calificacion,end=" ")
print()
promedio_parcial1=sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print(f"Promedio: {promedio_parcial1}")