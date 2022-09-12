"""
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 * Un constructor.
 * Los setters y getters para el nuevo atributo.
 * En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
   tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
   mayor de edad pero menor de 25 años y falso en caso contrario.
 * Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 * El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
   cuenta.
"""
from abc import ABC, abstractclassmethod
from ejercicio7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self,titular=None,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        if isinstance(bonificacion,(int,float)):
            self.__bonificacion=bonificacion
        else:
            print("La bonificación debe ser un número")
    
    def set_bonificacion(self,bonificacion):
        if isinstance(bonificacion,(int,float)):
            self.__bonificacion=bonificacion
        else:
            print("La bonificación debe ser un número")
    
    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_validado(self):
        titular=self.get_titular()
        if (titular.get_edad()>=18 and titular.get_edad()<=25):
            return True
        else:
            return False

    def retirar(self,cantidad):
        if self.es_titular_validado():
            if isinstance(cantidad, (int, float)):
                if cantidad > 0:
                    super().retirar(cantidad)
                else:
                    print("La cantidad debe ser un número positivo")
            else:
                print("La cantidad debe ser un número positivo")
        else:
            print("El titular no esta validado para retirar")

    def mostrar(self):
        print("Cuenta Joven")
        titular=self.get_titular()
        titular.mostrar()
        print(f"Saldo de cuenta: ${self.get_cantidad()}")
        print(f"Bonificacion {self.get_bonificacion()}%")

cuenta1=CuentaJoven()
cuenta1.set_titular("Pedro",25,33333333)
cuenta1.ingresar(99999)
cuenta1.retirar(999)
cuenta1.set_bonificacion(15)
print(cuenta1.es_titular_validado())
cuenta1.mostrar()