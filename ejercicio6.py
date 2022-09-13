"""
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 * Un constructor, donde los datos pueden estar vacíos.
 * Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 * mostrar(): Muestra los datos de la persona.
 * Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""


class Persona:

    def valida_nombre(funcion):
        def validacion(*args, **kwargs):
            if (args[1].isalpha() and not(args[1].isspace())):
                return funcion(*args,**kwargs)
            else:
                print ("Ingrese un nombre válido")
        return validacion

    def valida_edad(funcion):
        def validacion(*args, **kwargs):
            try:
                if (args[1] > 0 and args[1] < 130):
                    return funcion(*args,**kwargs)
                else:
                    print("Ingrese una edad válida")
            except Exception as error:
                print(f"Error: {error}")
                print("Ingrese una edad válida")
        return validacion

    def valida_DNI(funcion):
        def validacion(*args, **kwargs):
            try:
                if (args[1] > 0 and args[1] < 199999999):
                    return funcion(*args,**kwargs)
                else:
                    print("Ingrese un documento válido")
            except Exception as error:
                print(f"Error: {error}")
                print("Ingrese un documento válido")
        return validacion

    def __init__(self,nombre=None,edad=None,DNI=None):
        if (nombre==None):
            self.__nombre=nombre
        else:
            self.__nombre= self.set_nombre(nombre)
        if (edad==None):
            self.__edad=edad
        else:
            self.__edad=self.set_edad(edad)
        if (DNI==None):
            self.__DNI=DNI
        else:
            self.__DNI=self.set_DNI(DNI)
    
    @valida_edad
    def set_edad(self,edad):
        self.__edad=edad
        return edad
    
    def get_edad(self):
        return self.__edad

    @valida_nombre
    def set_nombre(self,nombre):
        self.__nombre=nombre
        return nombre
    
    def get_nombre(self):
        return self.__nombre

    @valida_DNI
    def set_DNI(self,DNI):
        self.__DNI=DNI
        return DNI
    
    def get_DNI(self):
        return self.__DNI

    def mostrar(self):
        print(f"{self.__nombre}, edad: {self.__edad} años, DNI Nº: {self.__DNI}")
    
    def Es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False