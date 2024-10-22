'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 21 de octubre de 2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola, ejercicio que recibe datos de profesores.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de profesores    *****")
nombre = input("Ingresa el nombre completo del profesor: ")#Esto recibe un String como dato de entrada
num_cubo = int(input("Ingresa el no. de cubículo: "))#Esto igual recibe un String pero al anteponer un int se realiza un cast de variables y lo convierte a entero
horas_trabajo = float(input("Cantidad de horas que imparte clases a la semana: "))#Esto igual recibe un String pero al anteponer un float se realiza un cast de variables y lo convierte a flotante
tiempo = input("¿Tiene más de 5 años en la UNSIJ (Si/No)?: ")

tiempo = tiempo.lower() == "si"#La función es_mujer.lower() convierte cualquier cadena en minuscula compara con "si" y devuelve un booleano, si no es igual regresa false


print()
print(f"El profesor {nombre} con el número de cubículo {num_cubo} imparte un total de {horas_trabajo:.2f} horas de clases a la semana. Además, tiene más de 5 años impartiendo clases: {tiempo}.")
#La función :.2f determina la cantidad de decimales que deseamos poner después del punto decimal