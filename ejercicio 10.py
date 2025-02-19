""" 
Crea una lista de cadenas a tu elección.
Imprime la lista original.
Aplica reverse() para invertir su orden.
Vuelve a imprimir la lista. """

import os

try:
    listaCadenas=["Moneyway", "Los Pulpos", "MMNF", "KR", "Kris R"]
    print("Lista original:", listaCadenas)
    for elemento in listaCadenas:
        print(elemento)
    os.system('pause')
    os.system('cls')
    
    listaCadenas.reverse()
    print("Lista invertida:", listaCadenas)
    for elemento in listaCadenas:
        print(elemento)
        
except Exception as error:
    print(f"Ha ocurrido un error: {error}")