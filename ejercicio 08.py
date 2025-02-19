""" 
Crea una lista con varios elementos repetidos, por ejemplo ["manzana", "pera", "manzana", "naranja", "manzana"].
Pide al usuario una fruta para contar cuántas veces aparece en la lista.
Usa count() y muestra el resultado.
Si la cuenta es 0, indica que la fruta no está en la lista. """

import os
randomList=["manzana", "pera", "manzana", "naranja", "manzana", "uva", "uva", "piña", "banano", "pera", "ciruela", "fresa", "fresa"]

try:
    fruta=input("Ingresa una el nombre de una fruta: ")
    if fruta.isdigit():
        raise ValueError("No se permiten números")
    cuentas=randomList.count(fruta)
    os.system('cls')

    if cuentas>0:
        print(f"La fruta {fruta} aparece {cuentas} veces.")
    else:
        print(f"La fruta {fruta} no está en la lista.")
except ValueError as ve:
    print(f'Error: {ve}')
