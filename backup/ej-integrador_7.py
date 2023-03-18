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

# %% EJERCICIO 7
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase: 
#  Un constructor, donde los datos pueden estar vacíos. 
#  Los setters y getters para cada uno de los atributos. 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
#  mostrar(): Muestra los datos de la cuenta. 
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser un número negativo.")
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.dni = dni
        else:
            print("El DNI debe tener 8 caracteres.")
    
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



 # %% EJECUTAR


def main():

    # EJERCICIO 7
    def ejercicio7():

      
        nueva_persona = Persona("Roberto", "Galán", 83)
        nueva_cuenta = Cuenta(nueva_persona.nombre, nueva_persona.edad, nueva_persona.dni, 1000)
       
        nueva_cuenta.mostrar()
       

    # Ejecuto el Ejercicio 7
    ejercicio7()


if __name__ == "__main__":
    main()
