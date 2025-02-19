""" 
Crea una lista con al menos 5 elementos a tu elección.
Define una función llamada limpiar_lista que reciba una lista y la vacíe usando clear().
Antes de llamar a la función, muestra la lista original.
Llama a la función y luego imprime la lista para confirmar que está vacía. """
import os
def limpiar_lista(lista):
    
    try:
        lista.clear()
    except Exception as borrar:
        print(f'Error al limpiar la lista: {borrar}')

listaAndres=["Cash", "Anuel", "Luar", "Hades66", "Trap"]
print("Lista original:")
for elemento in listaAndres:
    print(elemento)
os.system("pause")
os.system("cls")

try:
    limpiar_lista(listaAndres)
    print("Lista después de limpiar:", listaAndres)
except Exception as e:
    print(f'Ocurrió un error: {e}')