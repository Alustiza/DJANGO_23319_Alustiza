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

import os
"""
Módulo para proveer una interfaz para el sistema operativo.
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
    """
    Una clase que representa a una persona con nombre, edad y DNI.
    """
    def __init__(self, nombre="", edad=0, dni=""):
        """
        Constructor para la clase Persona.

        Args:
            nombre (str): El nombre de la persona. Puede estar vacío.
            edad (int): La edad de la persona. Por defecto, es 0.
            dni (str): El número de identificación de la persona. Puede estar vacío.

        """
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    @property
    def nombre(self):
        """
        Obtiene el nombre de la persona.

        Returns:
            str: El nombre de la persona.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """
        Establece el nombre de la persona.

        Args:
            nombre (str): El nombre de la persona.
        """
        self._nombre = nombre
    
    @property
    def edad(self):
        """
        Obtiene la edad de la persona.

        Returns:
            int: La edad de la persona >= 0
        """
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        """
        Establece la edad de la persona.

        Args:
            edad (int): La edad de la persona >= 0
        """
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser un número negativo.")
    
    @property
    def dni(self):
        """
        Obtiene el número de dni de la persona.

        Returns:
            str: El número de dni de la persona.
        """
        return self._dni
    
    @dni.setter
    def dni(self, dni): 
        """
        Establece el número de dni de la persona.

        Args:
            dni (str): El número de dni de la persona validado = 8 caracteres
        """
        if len(dni) == 8:
            self._dni = dni
        else:
            print("El DNI debe tener 8 caracteres.")
    
    def mostrar(self):
        """
        Muestra los datos de la persona.
        """
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("DNI:", self._dni)
    
    def es_mayor_de_edad(self):
        """
        Comprueba si la persona es mayor de edad. +18

        Returns:
            bool: True si la persona es mayor de edad, False en caso contrario.
        """
        print("Es mayor de edad:", self._edad >= 18)
        return 


class Cuenta(Persona):
    
    def __init__(self, nombre, edad, dni, cantidad=0):
        titular = super().__init__(nombre, edad, dni)
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

      
        nueva_persona = Persona("Dylan", 82, 28383849)
        nueva_cuenta = Cuenta(nueva_persona.nombre, nueva_persona.edad, nueva_persona.dni, -1000)
       
        nueva_cuenta.mostrar()
       

    # Ejecuto el Ejercicio 7
    ejercicio7()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
