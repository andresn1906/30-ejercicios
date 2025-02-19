""" 
Crea una lista de nombres de personas.
Pide al usuario un nombre o parte de él.
Haz una función buscar_personas que reciba la lista y el texto a buscar.
Dentro de la función, recorre la lista con un for:
    Si el nombre contiene el texto (usando lower() y in), imprímelo.
Prueba la función. """
import os
def buscar_personas(lista, texto):
    for nombre in lista:
        if texto.lower() in nombre.lower():
            print(nombre)
    
nombres=['Juan', 'Andrés', 'Camila', 'Felipe', 'Manuel', 'Sofía', 'Roberto']
while True:
    try:
        nombreA=input('Ingresa un nombre: ').title()
        if not nombreA.replace(' ', '').isalpha():
            raise ValueError('El nombre sólo puede contener letras.')
        buscar_personas(nombres, nombreA)
    except ValueError as ve:
        print(ve)
        os.system('pause')
        os.system('cls')
        