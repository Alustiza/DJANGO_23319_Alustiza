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
            dni (str): El número de identificación de la persona. El valor que se ingrese debe ser numérico y de 8 carácteres. 

        """
        while not nombre:
            print("////////////////////////////////")
            print("//////////   ERROR   ///////////")
            print("////////////////////////////////")
            print("El nombre no puede estar vacío.")
            nombre = input("Por favor, ingrese un nombre válido: ")
        print("////////////////////////////////")
        print("//////  OK. NOMBRE.   //////////")
        print("////////////////////////////////")
        self._nombre = nombre

        
        while edad <= 0:
            try:
                print("////////////////////////////////")
                print("////////// ERROR. EDAD /////////")
                print("////////////////////////////////")
                print("La edad debe ser mayor a cero.")
                edad = int(input("Por favor, ingrese su edad: "))
                if edad <= 0:
                    print("La edad debe ser mayor a cero.")
            except ValueError:
                print("La edad debe ser un número entero mayor a cero. Inténtelo nuevamente.")
        print("////////////////////////////////")
        print("////////  OK. EDAD.   //////////")
        print("////////////////////////////////")
        self._edad = edad

                 

        while not dni.isdigit() or len(dni) != 8:
            print("////////////////////////////////")
            print("////////// ERROR ///////////")
            print("////////////////////////////////")
            print("El DNI debe tener 8 caracteres numéricos.")
            dni = input("Ingrese el número de DNI: ")
            if not dni.isdigit() or len(dni) != 8:
                print("////////////////////////////////")
                print("////////// ERROR ///////////")
                print("////////////////////////////////")
                print("El DNI debe tener 8 caracteres numéricos.")
        print("////////////////////////////////")
        print("////////  OK. DNI.   //////////")
        print("////////////////////////////////")
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
        while not nombre:
            print("////////////////////////////////")
            print("//////////   ERROR   ///////////")
            print("////////////////////////////////")
            print("El nombre no puede estar vacío.")
            nombre = input("Por favor, ingrese un nombre válido: ")
        print("////////////////////////////////")
        print("//////  OK. NOMBRE.   //////////")
        print("////////////////////////////////")
        self._nombre = nombre

    @property
    def edad(self):
        """
        Obtiene la edad de la persona.

        Returns:
            int: La edad de la persona como entero positivo
        """
        return self._edad

    @edad.setter
    def edad(self, edad):
        """
        Establece la edad de la persona.

        Args:
            edad (int): La edad de la persona como entero positivo
        """
        while edad <= 0:
            try:
                print("////////////////////////////////")
                print("////////// ERROR. EDAD /////////")
                print("////////////////////////////////")
                print("La edad debe ser mayor a cero.")
                edad = int(input("Por favor, ingrese su edad: "))
                if edad <= 0:
                    print("La edad debe ser mayor a cero.")
            except ValueError:
                print("La edad debe ser un número entero mayor a cero. Inténtelo nuevamente.")
        print("////////////////////////////////")
        print("////////  OK. EDAD.   //////////")
        print("////////////////////////////////")
        self._edad = edad

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
        while not dni.isdigit() or len(dni) != 8:
            print("////////////////////////////////")
            print("////////// ERROR ///////////")
            print("////////////////////////////////")
            print("El DNI debe tener 8 caracteres numéricos.")
            dni = input("Ingrese el número de DNI: ")
            if not dni.isdigit() or len(dni) != 8:
                print("////////////////////////////////")
                print("////////// ERROR ///////////")
                print("////////////////////////////////")
                print("El DNI debe tener 8 caracteres numéricos.")
        print("////////////////////////////////")
        print("////////  OK. DNI.   //////////")
        print("////////////////////////////////")
        self._dni = dni


    def mostrar(self):
        """
        Muestra los datos de la persona.
        """
        print("")
        print("///////////////////////////////////")
        print("DATOS PERSONALES:")
        print("///////////////////////////////////")
        print("")
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("DNI:", self._dni)
        print("")

    def es_mayor_de_edad(self):
        """
        Comprueba si la persona es mayor de edad. +18

        Returns:
            bool: True si la persona es mayor de edad, False en caso contrario.
        """
        print("")
        print("Es mayor de edad (+18):", self._edad >= 18)
        print("")
        return

##############

class Cuenta:
    """
    Clase que crea una cuenta con un titular (una persona) y una cantidad de dinero (puede tener decimales).
    """

    def __init__(self, titular=None, cantidad=0):
        """
        Constructor para la clase Cuenta.

        Args:
            titular (Persona): La persona titular de la cuenta.
            cantidad (float): La cantidad de dinero en la cuenta. Por defecto, es 0. Puede tener decimales.
        """
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        """
        Obtiene la persona titular de la cuenta.

        Returns:
            Persona: La persona titular de la cuenta.
        """
        return self._titular

    @titular.setter
    def titular(self, titular):
        """
        Establece la persona titular de la cuenta.

        Args:
            titular (Persona): La persona titular de la cuenta.
        """
        self._titular = titular

    @property
    def cantidad(self):
        """
        Obtiene la cantidad de dinero en la cuenta.

        Returns:
            float: La cantidad de dinero en la cuenta.
        """
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self):
        """
        Establece la cantidad de dinero en la cuenta.

        Returns:
            float: La cantidad de dinero en la cuenta.
        """
        return self._cantidad

    def mostrar(self):
        """
        Muestra los datos de la cuenta.
        """
        print("")
        
        print("DATOS DE LA CUENTA")
        print("")
        print("TITULAR:")
        self._titular.mostrar()
        print("")
        print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
        print("")

    def ingresar(self, cantidad):
        """
        Ingresa una cantidad de dinero en la cuenta.

        Args:
            cantidad (float): La cantidad de dinero a ingresar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        """
        if cantidad > 0:
            self._cantidad += cantidad
            print("")
            print("///////////////////////////////////")
            print(f"INGRESO SOLICITADO: ${cantidad}")
            print("///////////////////////////////////")
            print("La solicitud de ingreso fue exitosa.")
            print("///////////////////////////////////")
            print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
            print("")
            return True
        else:
            print("")
            print("//////////////////////////////////////////")
            print("La solicitud de ingreso no se completó.")
            print("No se puede ingresar una cantidad negativa.")
            print("//////////////////////////////////////////")
            print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
            print("")

            return False

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta.

        Args:
            cantidad (float): La cantidad de dinero a retirar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        """
        if cantidad > 0:
            self._cantidad -= cantidad
            print("")
            print("///////////////////////////////////")
            print(f"RETIRO SOLICITADO: ${cantidad}")
            print("///////////////////////////////////")
            print("La solicitud de retiro fue exitosa.")
            print("///////////////////////////////////")
            print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
            print("")
            return True
        else:
            print("")
            print("//////////////////////////////////////////")
            print("La solicitud de retiro no se completó.")
            print("No se puede retirar una cantidad negativa.")
            print("//////////////////////////////////////////")
            print("")
            
            return False

 # %% EJECUTAR


def main():

    # EJERCICIO 7
    def ejercicio7():
        """
        Función que ejecuta el Ejercicio 7 del programa. 
        Crea una nueva Cuenta con un titular utilizando la clase Persona.
        Le solicita al usuario que ingrese el nombre, edad y dni. 
        Muestra la información de la cuenta recién creada. 
        Realiza una solicitud de retiro y vuelve a mostrar la información de la cuenta. Se permiten cantidades en números negativos.
        Luego, intenta una solicitud de ingreso con una cantidad negativa, para mostrar el mensaje de error.
        Por último se realiza una solicitud de ingreso y se vuelve a mostrar la información de la cuenta.
        """

    print("CREAR NUEVA CUENTA")
    print("Ingrese los datos del titular de la cuenta:")
    
    
    
    # Prueba creando una Persona sin enviar valores para los atributos
    titular = Persona()

     # Prueba creando una Persona enviando valores para los atributos
    #titular = Persona("RitaLee",23,"23222222")
    nueva_cuenta = Cuenta(titular, 0)

    # Muestra los datos de la cuenta
    nueva_cuenta.mostrar()

    # Solicitud de retiro a partir del valor que ingresa el usuario
    print("SOLICITUD DE RETIRO")
    cantidad_retiro = int(input("Ingrese la cantidad a retirar de su cuenta: $"))
    nueva_cuenta.retirar(cantidad_retiro)

    # Solicitud de ingreso a partir del valor que ingresa el usuario
    print("SOLICITUD DE INGRESO")
    cantidad_ingreso = int(input("Ingrese la cantidad a ingresar en su cuenta: $"))
    nueva_cuenta.ingresar(cantidad_ingreso)

    # Muestra los datos de la cuenta
    nueva_cuenta.mostrar()


    # Ejecuto el Ejercicio 7
    ejercicio7()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

# %%
