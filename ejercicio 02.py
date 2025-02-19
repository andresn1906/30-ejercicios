""" 
Crea una lista llamada numeros con algunos valores iniciales, por ejemplo: [1, 2, 3].
Pide al usuario que ingrese tres números adicionales separados por espacio y conviértelos a enteros.
Usa extend() para agregar estos nuevos números a la lista numeros.
Imprime la lista final. """
import os
numeros=[1, 2, 3]
while True:
    print('Ingreso de nuevos números')
    while True:
        numerosExtra=input('Ingresa tus tres números separados c/u por espacios: ').split()
        if len(numerosExtra)!=3:
            print('Debes separar cada número por un espacio')
            continue
        try:
            if all(num.isdigit() for num in numerosExtra):
                if all(int(num)>3 for num in numerosExtra):
                    numeros.extend([int(numero) for numero in numerosExtra])
                    break
                else:
                    print('Ingrese tres números enteros mayores a 3')
            else:
                raise ValueError("No se permiten letras")
        except ValueError as ve:
            print(f'Error: {ve}')
        except Exception as e:
            print(f'Ocurrió un error: {e}')
        os.system('cls')
    print(numeros)
    if input("¿Deseas reiniciar? (s/n): ").lower()!='s':
        print('Fin')
        break
    else:
        numeros=[1, 2, 3]
    os.system('cls')
