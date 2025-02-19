""" 
Crea una lista de tareas vacía.
Mediante un ciclo while True , muestra un menú con:
    1. Agregar tarea
    2. Mostrar tareas
    3. Eliminar tarea
    4. Salir
Usa match para cada opción.
    Opción 1: pide la descripción de la tarea y agrégala con append().
    Opción 2: recorre la lista e imprime cada tarea.
    Opción 3: pide la descripción de la tarea y si está en la lista, elimínala con remove(). Si no está, indica que no existe.
    Opción 4: rompe el ciclo (break).
Verifica el correcto funcionamiento del menú. """

import os
tareas=[]

while True:
    print('''
        >>>> Menú de Tareas <<<<
          1. Agregar tarea
          2. Mostrar tareas
          3. Eliminar tarea
          4. Salir.
        ''')
    try:
        opcion=int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                descripcion=input('Ingresa la descripción: ')
                tareas.append(descripcion)
                print('Tarea agregada.')
                os.system('pause')
                os.system('cls')
            case 2:
                if tareas:
                    print('Lista de tareas:')
                    for tarea in tareas:
                        print(f'- {tarea}')
                else:
                    print('No hay tareas.')
                os.system('pause')
                os.system('cls')
            case 3:
                descripcion=input('Ingresa la descripción de la tarea a eliminar: ')
                if descripcion in tareas:
                    tareas.remove(descripcion)
                    print('Tarea eliminada.')
                else:
                    print('La tarea no existe en la lista.')
                os.system('pause')
                os.system('cls')
            case 4:
                print('Saliendo del programa...')
                break
            case _:
                print('Opción inválida.')
    except ValueError:
        print('Ingresa una opción válida.')