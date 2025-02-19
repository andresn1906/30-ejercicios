""" 
Crea una lista llamada lista_original con varios elementos.
Asigna lista_copia = lista_original.copy().
Modifica la lista original (por ejemplo, cambia un elemento).
Imprime ambas listas para comprobar que la copia se mantiene independiente. """

import os
lista_original=["Ryan Castro", "Blessd", "Feid", "Yovngchimi"]
lista_copia=lista_original.copy()

lista_original[2]="Anuel AA, el Dios del tra'"

print("Lista original: ")
for elemento in lista_original:
    print(elemento)
    
print('\n')   
print("2da Lista: ")
for elemento in lista_copia:
    print(elemento)