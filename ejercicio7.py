"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 * Un constructor, donde los datos pueden estar vacíos.
 * Los setters y getters para cada uno de los atributos. 
   El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 * mostrar(): Muestra los datos de la cuenta.
 * ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
   negativa, no se hará nada.
 * retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

from abc import ABC, abstractclassmethod
from ejercicio6 import Persona

class Cuenta(ABC):
    
    def __init__(self,titular=None,cantidad=0):
        if titular==None:
            self.__titular=Persona()
        else:
            if isinstance(titular,Persona):
                self.__titular=titular
            else:
                print("La persona debe ser un objeto de Persona")
        if (cantidad != 0):
            if isinstance(cantidad, (int, float)):
                self.__cantidad=cantidad
            else:
                print("Debe ingresar una cantidad válida")
        else:
            self.__cantidad=float(0)

    def set_titular(self,nombre,edad,dni):
        self.__titular.set_nombre(nombre)
        self.__titular.set_edad(edad)
        self.__titular.set_DNI(dni)
    
    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def ingresar(self,cantidad):
        if isinstance(cantidad, (int, float)):
            if cantidad > 0:
                self.__cantidad = self.__cantidad + cantidad
        else:
            print("La cantidad debe ser un número")

    def retirar(self,cantidad):
        if isinstance(cantidad, (int, float)):
            if cantidad > 0:
                self.__cantidad = self.__cantidad - cantidad
            else:
                print("La cantidad debe ser un número positivo")
        else:
            print("La cantidad debe ser un número positivo")

    def mostrar(self):
        self.__titular.mostrar()
        print(f"Saldo de cuenta: ${self.get_cantidad()}")



    
