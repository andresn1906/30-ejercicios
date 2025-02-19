""" 
Crea una lista con varios colores, por ejemplo ["rojo", "azul", "verde", "amarillo", "negro"].
Pide al usuario que ingrese un color.
Usa un "(try/except)" para manejar posibles errores:
Dentro del try, usa index() para obtener la posición del color ingresado.
Muestra la posición en pantalla.
En el except, muestra un mensaje indicando que el color no está en la lista. """

import os
colores=["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco", "Violeta"]
nuevoColor=input("Por favor ingresa un color: ").capitalize()
os.system('cls')

try:
    pos=colores.index(nuevoColor)
    print(f"El color {nuevoColor} está en la posición {pos}")
except ValueError:
    print(f"El color {nuevoColor} no está en la lista.")
os.system('pause')
os.system('cls')

print("Lista de colores: ")
for elemento in colores:
    print(elemento)