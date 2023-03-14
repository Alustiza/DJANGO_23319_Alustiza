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

# %% EJERCICIO 6
# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

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





 # %% EJECUTAR


def main():

    # EJERCICIO 6
    def ejercicio6():
        nueva_persona = Persona()
        
        nueva_persona.mostrar()
        print(nueva_persona.es_mayor_de_edad())
    
       

    # Ejecuto el Ejercicio 6
    ejercicio6()


if __name__ == "__main__":
    main()
