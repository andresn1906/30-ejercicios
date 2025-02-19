""" 
Crea una función evaluar_estado que reciba una nota (entero) como parámetro.
Dentro de la función:
    Primero, usa un if para verificar si la nota es válida (0 a 10). Si no lo es, retorna "Nota inválida".
    Si es válida, usa match nota:
     para imprimir:
        10: "Excelente"
        8 o 9: "Muy bien"
        6 o 7: "Bien"
        4 o 5: "Regular"
        _: "Reprobado"
Prueba la función con notas ingresadas por el usuario. """
import os
def evaluar_estado(nota):
    if nota<0 or nota>10:
        return "Nota inválida"
    match nota:
        case 4 | 5:
            return "Regular"
        case 6 | 7:
            return "Bien"
        case 8 | 9:
            return "Muy bien"
        case 10:
            return "Excelente"
        case _:
            return "Reprobado"

while True:
    try:
        nota = int(input("Ingresa la nota: "))
        os.system('cls')
        print(evaluar_estado(nota))
    except ValueError:
        print("Ingresa un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")