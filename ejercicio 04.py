""" 
Crea una lista llamada animales con valores a tu elección (ej. ["perro", "gato", "elefante", "tigre"]).
Pide al usuario un nombre de animal para eliminar de la lista.
Antes de eliminar, utiliza una estructura if para verificar si el animal está en la lista.
    Si está, usa remove() para quitarlo.
    Si no está, muestra un mensaje indicando que no se encontró.
Imprime la lista final. """

try:
    animales = ["perro", "gato", "elefante", "tigre"]
    eliminar = input("Ingresa el nombre del animal a eliminar (si se encuentra en la lista): ")
    if eliminar.isdigit():
        raise ValueError("No se permiten números")
    if eliminar in animales:
        animales.remove(eliminar)
        print(f"{eliminar} ha sido eliminado de la lista.")
    else:
        print(f"{eliminar} no se encontró en la lista.")
    print(f"Listado de animales: {animales}")
except ValueError as ve:
    print(f'Error: {ve}')
except Exception as e:
    print(f'Ocurrió un error: {e}')