""" 
Pide al usuario que ingrese un número par.
Si no es par, vuelve a pedirlo (ciclo while).
Cuando finalmente ingrese un número par, añádelo a una lista e imprime la lista.
Repite el proceso para 3 números par. 
"""
evenNumbers=[]
while len(evenNumbers)<=3:
    try:
        number=int(input("Digita tu número par: "))
        if number%2==0:
            evenNumbers.append(number)
            print(f"{number} agregado con éxito")
        else:
            print("Número impar, vuelve a intentar")
    except ValueError as ve:
        print("Ingresa un número entero par ")

print(f"\nLista final de 'Números Pares': {evenNumbers} ")