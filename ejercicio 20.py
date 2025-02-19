""" Genera una lista de números del 1 al 10.
Crea una función filtrar_lista(numeros, tipo):
    Si tipo es "pares", devuelve una nueva lista con solo los números pares.
    Si tipo es "impares", devuelve solo los impares.
    Usa un ciclo for y un if para filtrar.
Imprime los resultados para ambos casos. """

numeros=list(range(1, 11))

def filtrar_lista(numeros, tipo):
    if tipo=='pares':
        return[num for num in numeros if num%2==0]
    elif tipo=='impares':
        return[num for num in numeros if num%2!=0]
    else:
        raise ValueError('Comando inválido. Usa "pares" o "impares')

try:
    pares=filtrar_lista(numeros, 'pares')
    impares=filtrar_lista(numeros, 'impares')
    print('Pares:', pares)
    print('Impares:', impares)
except (ValueError) as ve:
    print({ve})
