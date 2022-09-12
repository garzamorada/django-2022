"""
1. Escribir una función que calcule el máximo común divisor entre dos números.
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""

from math import floor


def MCD(numero1,numero2): #Maximo comun divisor por metodo de euclides
    if (numero1 == 0):
        return numero2
    elif (numero2 == 0):
        return numero1
    else:
        if (numero1 >= numero2):
            mayor = numero1
            menor = numero2
        else:
            mayor = numero2
            menor = numero1
        while (menor != 0):
            resultado = floor(mayor/menor)
            resto = mayor - (menor * resultado)
            mayor = menor
            menor = resto
        return mayor


def mcm(numero1,numero2): #minimo comun multiplo 
    return int((numero1/MCD(numero1,numero2)) * numero2)

print("Ingrese el primero número: ")
numero1 = int(input())
print("Ingrese el segundo número: ")
numero2 = int(input())
print(f"El maximo comun divisor entre {numero1} y {numero2} es {MCD(numero1,numero2)}")
print(f"El mínimo comun múltiplo entre {numero1} y {numero2} es {mcm(numero1,numero2)}")


def CuentaPalabras(frase): #devuelve un diccionario con las palabras y su frecuencia
    diccionario={}
    frase=frase.lower()
    lista=frase.split(' ')
    for palabra in lista:
        cantidad = lista.count(palabra)
        diccionario[palabra]=cantidad
    return diccionario

def PalabraMasRepetida(diccionario): #devuelve la palbra mas repetida
    items=diccionario.items()
    maximo = 0
    tupla=()
    for item in items:
        cantidad = item[1]
        if cantidad > maximo:
            maximo = cantidad
            tupla = item
    return tupla


print("Ingrese la frase a convertir en diccionario:")
frase = input()
diccionario=CuentaPalabras(frase)
print("el diccionario es: ")
print(diccionario)
tupla=PalabraMasRepetida(diccionario)
print(f"la palabra mas repetida es: ")
print(tupla)