"""
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""

def get_int():
    bandera=0
    while (bandera != 1):
        print("ingrese un numero entero: ")
        cadena=input()
        try:
            numero=int(cadena)
        except ValueError:
            bandera=0
            print("Error: Sólo se aceptan números enteros")
        except Exception as error:
            bandera=0
            print(f"Se produjo un error: {error}")
        else:
            bandera=1
    return numero

print("funcion con while")
print(f"El número ingresado es {get_int()}")

def get_int():
    print("ingrese un numero entero: ")
    cadena=input()
    try:
        numero=int(cadena)
        return numero
    except ValueError:
        print("Error: Sólo se aceptan números enteros")
        return get_int()
    except Exception as error:
        print(f"Se produjo un error: {error}")
        return get_int()
        
print("")
print("funcion recursiva")
print(f"El número ingresado es {get_int()}")
