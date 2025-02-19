""" 
Partiendo de la agenda del ejercicio anterior, crea una función llamada mostrar_contactos que reciba la lista de contactos y un filtro (una cadena) para el nombre.
La función recorre la lista de contactos (usando un ciclo for):
    Si el nombre del contacto contiene la cadena del filtro (usa funciones de cadena como in, lower()), imprime los datos del contacto.
Prueba la función solicitando al usuario un filtro. """

def mostrar_contactos(lista, filtro):
    try:
        filtro = filtro.lower()
        for contacto in lista:
            if filtro in contacto['nombre'].lower():
                print(contacto)
    except Exception as e:
        print(f"Error inesperado: {e}")
try:
    contacts = [
        {'nombre': 'Juan', 'número celular': '1234567890'},
        {'nombre': 'Ana', 'número celular': '0987654321'}
    ]
    filtro = input('Ingrese el filtro para buscar contactos: ')
    mostrar_contactos(contacts, filtro)
except Exception as e:
    print(f"Error: {e}")