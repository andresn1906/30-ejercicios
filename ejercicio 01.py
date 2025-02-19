""" 
Crea una lista vacía llamada frutas.
Pide al usuario que ingrese 3 frutas y añádelas a la lista usando append().
Muestra la lista resultante.
Crea una función definida por el usuario que reciba una lista y la imprima en pantalla.
Llama a la función pasando la lista frutas. """

import os

def listaFrutas(lista):
    for item in lista:
        print(item.title())

while True:
    frutas = []
    print('A continuación ingrese sus frutas')
    os.system('pause')
    os.system('cls')
    for _ in range(3):
        while True:
            try:
                fruta = input('Indique la fruta: ')
                if fruta.isdigit():
                    raise ValueError("No se permiten números")
                if fruta.isalpha() and len(fruta) >= 3:
                    frutas.append(fruta)
                    break
                else:
                    print("Ingrese sólamente las frutas")
            except ValueError as ve:
                print(f'Error: {ve}')
            except Exception as e:
                print(f'Ocurrió un error: {e}')
    print([fruta.title() for fruta in frutas])
    listaFrutas(frutas)
    os.system('pause')
    os.system('cls')
    if input("¿Desea continuar? (s/n): ").lower()!='s':
        break