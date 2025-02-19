""" 
Crea una lista de números desordenados: por ejemplo [3, 8, 1, 7, 2].
Aplica sort() para ordenarla de forma ascendente.
Imprime la lista resultante.
Pide al usuario que indique si desea el orden
ascendente o descendente
Si indica descendente, vuelve a aplicar sort(reverse=True).
Imprime el resultado final. """

import os

try:
    randomNumList=[7, 8, 6, 5, 2, 3, 0]
    randomNumList.sort()
    print("La lista ordenada ascendentemente es:", randomNumList)
    os.system('cls')
    
    orden=input("Deseas el orden ascendente o descendente? (a/d): ")
    if orden.lower()=='d':
        randomNumList.sort(reverse=True)
        print("La lista ordenada descendentemente es:", randomNumList)
        for elemento in randomNumList:
            print(elemento)
    elif orden.lower()=='a':
        print("Resultado lista final:", randomNumList)
        for elemento in randomNumList:
            print(elemento)
    else:
        raise ValueError("Opción inválida. Ingresa 'a' para ascendente o 'd' para descendente.")
except ValueError as ve:
    print(f"Error: {ve}")
