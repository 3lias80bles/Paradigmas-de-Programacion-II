'''
Nombre: Sergio Elías Robles Ignacio
Fecha: 18 de octubre de 2024
Descripción: En este trabajo se muestra el funcionamiento de un operador lógico.
'''

#Se definimos los datos correctos para el acceso.
usuario = "Alumnos"     #Usuario correcto.
contr = "Python"        #Contraseña correcta.

#Se solicita al usuario ingresar usuario y cntraseña.
us = input("Ingresa tu usuario: ")
co = input("Ingresa tu contraseña: ")

#Se verifica si el usuario y la contraseña ingresados coinciden con los correctos y nos almacena un booleano (True/False).
us = us == usuario
co = co == contr

#Se muestra un mensaje que indica si el acceso es correcto (True) o incorrecto (False).
print(f"El acceso es correcto: {us and co}")
