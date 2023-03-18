#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# < ^ >  { }  [ ] ' ' [' ']
"""
CODO A CODO: DJANGO
AÑO: 2023
COMISIÓN: 23319
ACTIVIDAD DE INTEGRACIÓN

@author: pabloalustiza
"""

# %% EJERCICIO 8
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. 
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase: 
#  Un constructor. 
#  Los setters y getters para el nuevo atributo. 
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        
        if edad >= 0:
            self.nombre = nombre
            self.edad = edad
            self.dni = dni
        else:
            print("La edad no puede ser un número negativo. De manera temporal le asignamos el valor 0")
            self.nombre = nombre
            self.edad = 0
            self.dni = dni
        
    

    def set_nombre(self, nombre):
        self.nombre = nombre


    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser un número negativo. De manera temporal le asignamos el valor 0")

    def get_edad(self):
        return self.edad
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.dni = dni
        else:
            print("El DNI debe tener 8 caracteres.")

            
    def get_dni(self):
        return self.dni
    
    
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta(Persona):
    
    def __init__(self, nombre, edad, dni, cantidad=0):
        super().__init__(nombre, edad, dni)
        self.__cantidad = cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        super().mostrar()
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, nombre, edad, dni, cantidad, bonificacion=0):
        print("")

        if edad  < 18 :
            print("Lo siento, eres menor de 18 años y no puedes abrir una cuenta con nosotros.")
            super().__init__(nombre, edad, dni)
            self.bonificacion = 0
            self.tipoCuenta = "Menor 18 años:"
        else:
            if edad > 25:
                print("Lo siento, eres mayor de 25 años y no calificas para la bonificación de la Cuenta Joven. Pero calificas para las Cuentas +25.")
                super().__init__(nombre, edad, dni, cantidad)
                self.bonificacion = 0
                self.tipoCuenta = "Cuenta +25 años:"

            else:
                super().__init__(nombre, edad, dni, cantidad)
                self.bonificacion = bonificacion/100
                self.tipoCuenta = "Cuenta Joven:"
        
    def set_bonificacion(self, bonificacion):     
        if self.es_titular_valido():
            self.bonificacion = bonificacion / 100
        else:
            if self.get_edad() > 25:
                # print("Lo siento, no se puede asignar una bonificación a una cuenta para mayores de 25 años.")
                self.bonificacion = 0 / 100
            elif self.edad < 18:
                # print("Lo siento, no se puede asignar una bonificación a una cuenta para menores de 18 años.")
                self.bonificacion = 0 / 100
       
            

    def get_bonificacion(self):
        return self.bonificacion
    
    def mostrar(self):
        print("")
        print(self.tipoCuenta)
        print("")
        # print("Nombre:", self.get_nombre())
        # print("Edad:", self.get_edad())
        # print("DNI:", self.get_dni())
        # print("Cantidad:", self.get_cantidad())
        super().mostrar()
        print("Bonificación:", "{:.0f}%".format(self.bonificacion * 100))
        print("")

    def es_titular_valido(self):
        return 18 <= self.get_edad() <= 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            print("El retiro de", cantidad, "se realizó correctamente.")

        else:
            print("El titular no es válido para retirar dinero.")



    


 # %% EJECUTAR


def main():

    # EJERCICIO 8
    def ejercicio8():

      


        # Crear un objeto CuentaJoven
        cuenta_joven_Lima = CuentaJoven("Lima",21, "50343587", 777)

        # Asignar un valor de bonificacion a la Cuenta Joven
        cuenta_joven_Lima.set_bonificacion(42)

        cuenta_joven_Lima.mostrar()
        print("El titular califica para una Cuenta Joven:", cuenta_joven_Lima.es_titular_valido())
        print("")

        cuenta_joven_Lima.retirar(10)

        cuenta_joven_Lima.mostrar()



       

    # Ejecuto el Ejercicio 8
    ejercicio8()


if __name__ == "__main__":
    main()
