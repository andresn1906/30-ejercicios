""" 
Pide al usuario ingresar 5 números.
Guárdalos en una lista.
Define una función llamada clasificar números que reciba la lista y:
    Imprima cuáles son pares.
    Imprima cuáles son impares.
Dentro de la función, utiliza un ciclo for y un condicional if para la clasificación.
Llama a la función y muestra la salida. """

def clasificarNumeros(lista):
    try:
        pares=[]
        impares=[]
        for numero in lista:
            if not isinstance(numero, int):
                raise ValueError("La lista contiene un valor que no es un número.")
            if numero%2==0:
                pares.append(numero)
            else:
                impares.append(numero)
        print(f'Números pares: {pares}')
        print(f'Números impares: {impares}')
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

try:
    numeros=[]
    for _ in range(5):
        while True:
            try:
                numero = int(input('Ingresa un número: '))
                numeros.append(numero)
                break
            except ValueError:
                print('Ingresa un número válido.')

    clasificarNumeros(numeros)
except Exception as error:
    print(f"Error inesperado: {error}")