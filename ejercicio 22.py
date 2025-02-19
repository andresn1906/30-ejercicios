""" 
Crea una función llamada sumar(a, b) que retorne la suma de dos números.
En la función principal, pide al usuario dos números, llama a sumar(a, b) y muestra el resultado.
Pide al usuario si desea realizar otra operación (sí/no). Si la respuesta es "sí", repite el ciclo. 
"""
def sumar_ab(a, b):
    return a+b

while True:
    try:
        n1=float(input("Digita un número: "))
        n2=float(input("Digita otro número: "))
        sum=sumar_ab(n1, n2)
        print(f"El resultado de la suma entre {n1} y {n2} es {sum}")
    except ValueError:
        print("Ingresa sólo números")
        continue_=input("¿Deseas realizar otra operación (S/N)?: ").strip().upper()
        if continue_!="S":
            print("Fin")
            break
            
        
        