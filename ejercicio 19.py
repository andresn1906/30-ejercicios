""" Pide al usuario que ingrese una frase.
Convierte la frase a lista de palabras usando split().
Muestra la lista obtenida.
Une la lista de nuevo en una cadena usando join(), separando por espacio.
Imprime la cadena resultante. """

import os

frase=input('Digita una frase cualquiera: ')
lista=frase.split()
os.system('pause')
os.system('cls')

print(f'Lista de palabras: {lista} ')
os.system('pause')
os.system('cls')

cadena_unida=' '.join(lista)


print(f'La cadena resultante es: {cadena_unida}')