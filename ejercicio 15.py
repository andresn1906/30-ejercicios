""" 
Crea una variable opcion que el usuario ingresará (valor entero).
Usa una estructura match opcion:
    para manejar estos casos:
        1: imprimir "Seleccionaste opción 1"
        2: imprimir "Seleccionaste opción 2"
        _: imprimir "Opción inválida"
Muestra cómo se comporta el programa según la opción elegida. """

try:
    opcion=int(input('Selecciona una opción (1/2): '))
    match opcion:
        case 1:
            print('Seleccionaste opción 1')
        case 2:
            print('Seleccionaste opción 2')
        case _:
            print('Opción inválida')
except ValueError:
    print('Ingresa un número válido.')