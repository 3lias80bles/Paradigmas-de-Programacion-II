'''
Nombre: Sergio Elías Robles Ignacio
Fecha: 17 de octubre de 2024
Descripción: En este trabajo se muestra el funcionamiento de un operador lógico.
'''

print("*** Comunidad de la UNSIJ ***")
# Se solicitan datos, uno de tipo booleano y otro de tipo String.
profesor = input("¿Eres profesor de la UNSIJ (Sí/No)? ")
alumno = input("¿Eres alumno de la UNSIJ (Sí/No)? ")

#Se convierte la cadena a minúsculas y la compara, asignando un valor booleano a la variable (True/False).
profesor = profesor.lower() == "sí"
alumno = alumno.lower() == "sí"
# "or" verifica si al menos uno es verdadero para determinar si forma parte de la comunidad.
print(f"¿Forma parte de la comunidad de la UNSIJ? {profesor or alumno}")
