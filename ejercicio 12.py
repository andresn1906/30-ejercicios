""" 
Crea una lista vacía para almacenar contactos.
Cada contacto será un diccionario con {"nombre": <str>, "tel": <str>}.
Crea una función llamada aggContacto que reciba la lista y agregue un nuevo contacto a partir de datos ingresados por el usuario.
La función debe usar append() para insertar el diccionario.
Muestra la lista de contactos después de cada inserción. """

contacts = []

def aggContacto(lista):
    try:
        nombre=input('Ingrese el nombre del contacto: ').capitalize()
        if any(char.isdigit() for char in nombre):
            raise ValueError("Ingresa sólo palabras con letras.")
        
        while True:
            tel=input('Ingrese el teléfono del contacto: ')
            if not tel.isdigit():
                print("Sólo puede contener números el celular.")
            elif len(tel)!=10:
                print("El celular debe tener 10 números.")
            else:
                break
        
        contacto={'nombre': nombre, 'número celular': tel}
        lista.append(contacto)
        print('Contacto agregado:', contacto)
        print('Lista de contactos actualizada: ')
        for c in lista:
            print(c)
    except ValueError as ve:
        print(f"{ve}")

aggContacto(contacts)
aggContacto(contacts)