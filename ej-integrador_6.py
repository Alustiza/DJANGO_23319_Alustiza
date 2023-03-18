#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# < ^ >  { }  [ ] ' ' [' ']
"""
CODO A CODO: DJANGO
AÑO: 2023
COMISIÓN: 23319
ACTIVIDAD DE INTEGRACIÓN

Este módulo define una clase Persona que tiene los atributos: nombre, edad y DNI. 
Se definen getters y setters para acceder a esos valores como si fueran atributos.
Se escribieron dos métodos: 
- mostrar los datos de la persona 
- validad si la persona es mayor de edad (+18)

@author: pabloalustiza

"""

import os
"""
Módulo para proveer una interfaz para el sistema operativo.
Se utiliza para limpiar la pantalla antes de ejecutar main()
"""

# %% EJERCICIO 6
# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

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





 # %% EJECUTAR


def main():
    """

    Función principal que ejecuta el programa y su clase Persona

    """
    # EJERCICIO 6
    def ejercicio6():
        nueva_persona = Persona("richard",-10,29898090)
        
        nueva_persona.mostrar()
        nueva_persona.es_mayor_de_edad()
       

    # Ejecuto el Ejercicio 6
    ejercicio6()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
