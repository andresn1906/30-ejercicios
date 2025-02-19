""" 
Crea una lista con números del 1 al 5.
Crea un menú usando un ciclo que pregunte al usuario:
    1. Hacer pop sin índice (pop al final)
    2. Hacer pop con índice
    3. Salir
En el caso 1, haz pop() sin argumentos para extraer el último elemento y muéstralo en pantalla.
En el caso 2, pide al usuario el índice y haz pop(indice). Muestra el elemento extraído.
En cada extracción, imprime la lista resultante.
Finaliza cuando el usuario elija la opción 3. """
import os
numeros=[1, 2, 3, 4, 5]
while True:
    print("\nMenú:")
    print("1. Hacer pop sin índice (pop al final)")
    print("2. Hacer pop con índice")
    print("3. Salir")
    opciones=input("Elige una opción: ")

    if opciones=='1':
        if numeros:
            elemento=numeros.pop()
            print(f"Elemento extraído: {elemento}")
        else:
            print("Lista está vacía.")
    elif opciones=='2':
        try:
            indice=int(input("Ingresa el índice: "))
            if 0<=indice<len(numeros):
                elemento=numeros.pop(indice)
                print(f"Elemento extraído: {elemento}")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except IndexError:
            print("Índice fuera de rango.")
        except Exception as e:
            print(f'Ocurrió un error: {e}')
    elif opciones=='3':
        print("Saliendo...")
        break
    else:
        os.system("cls")
        print("Opción inválida. Escoge entre las opciones disponibles (1, 2 o 3).")
    print(f"Lista resultante: {numeros}")