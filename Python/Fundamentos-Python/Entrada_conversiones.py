'''
Nombre: Sergio Elias Robles Ignacio
Fecha: 21 de octubre de 2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")#Esto recibe un String como dato de entrada
semestre = int(input("Ingresa el no. de semestre: "))#Esto igual recibe un String pero al anteponer un int se realiza un cast de variables y lo convierte a entero
promedio = float(input("Ingresa el promedio: "))#Esto igual recibe un String pero al anteponer un float se realiza un cast de variables y lo convierte a flotante
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"#La función es_mujer.lower() convierte cualquier cadena en minuscula, compara con "si" y devuelve un booleano

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
#La función :.2f determina la cantidad de decimales que deseamos poner después del punto decimal.