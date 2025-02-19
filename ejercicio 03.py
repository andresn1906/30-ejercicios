""" 
Crea una lista llamada lenguajes que contenga ["Python", "C", "Java"].
Pide al usuario un nuevo lenguaje de programación.
Usa insert() para colocar el nuevo lenguaje en la posición 1 de la lista.
Muestra el resultado final. """

try:
    lenguajes=["Python", "C", "Java"]
    nuevoLenguaje=input("Ingresa un nuevo lenguaje de programación: ")
    if nuevoLenguaje.isdigit():
        raise ValueError("Digita solamente el lenguaje de programación")
    lenguajes.insert(1, nuevoLenguaje)
    print("Nueva lista de lenguajes:", lenguajes)
except ValueError as ve:
    print(f'Error: {ve}')
except Exception as e:
    print(f'Ocurrió un error: {e}')


