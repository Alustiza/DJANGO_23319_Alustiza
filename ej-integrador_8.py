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

##############

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion=0):
        self._titular=titular
        if titular.edad  < 18 :
            print("Lo siento, eres menor de 18 años y no puedes abrir una cuenta con nosotros.")
            super().__init__(titular)
            self._bonificacion = 0
            self.tipoCuenta = "CUENTA NO ACTIVA. Menor 18 años. "
        else:
            if titular.edad > 25:
                print("Lo siento, eres mayor de 25 años y no calificas para la bonificación de la Cuenta Joven. Pero calificas para las Cuentas +25.")
                super().__init__(titular, cantidad)
                self._bonificacion=0
                self.tipoCuenta = "CUENTA +25 AÑOS ACTIVA"

            else:
                super().__init__(titular, cantidad)
                self._bonificacion = bonificacion
                self.tipoCuenta = "CUENTA JOVEN ACTIVA"

    @property
    def bonificacion(self):
        """
            Obtiene la bonificación en la cuenta.

            Returns:
                %: La bonificación en la cuenta.
            """
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self):
        """
            Obtiene la bonificación en la cuenta.

            Returns:
                %: La bonificación en la cuenta.
            """
        return self._bonificacion

    def es_titular_valido(self):
        return 18 <= self.titular.edad <= 25      
            
    def mostrar(self):
        """
        Muestra los datos de la cuenta.
        """
        print("")
        print("Tipo de Cuenta: ",self.tipoCuenta)
        print("¿Titular válido Cuenta Joven? ",self.es_titular_valido())
        print("")
        print("DATOS DE LA PERSONA:")
        print("")
        print("Nombre: ",self._titular.nombre)
   
        print("Edad: ",self._titular.edad)

        print("DNI: ",self._titular.dni)

        print("")
        print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
        print("")
        print("BONIFICACIÓN:", "{:.0f}%".format(self._bonificacion))
        print("")
      
        print("")

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta.

        Args:
            cantidad (float): La cantidad de dinero a retirar.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        """
        if self.es_titular_valido() == True:
            if cantidad > 0:
                self._cantidad -= cantidad
                print("")
                print("///////////////////////////////////")
                print(f"RETIRO SOLICITADO: ${cantidad}")
                print("///////////////////////////////////")
                print("///////////////////////////////////")
                print("//////  OK.   /////////////////////")
                print("////////////////////////////////")
                print("La solicitud de retiro fue exitosa.")
                print("///////////////////////////////////")
                print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
                print("")
                return True
            else:
                print("")
                print("///////////////////////////////////")
                print(f"RETIRO SOLICITADO: ${cantidad}")
                print("///////////////////////////////////")
                print("///////////////////////////////////////////")
                print("////////// ERROR. /////////////////////////")
                print("///////////////////////////////////////////")
                print("La solicitud de retiro no se completó.")
                print("Titular No Válido de Cuenta Joven.")
                print("///////////////////////////////////")
                print(f"CANTIDAD ACTUALIZADA EN CUENTA: ${self._cantidad}")
                print("")
                
                return False
        else:
            print("")
            print("///////////////////////////////////////////")
            print("////////// ERROR. /////////////////////////")
            print("///////////////////////////////////////////")
            print("// La solicitud de retiro no se completó. /")
            print("//////////////////////////////////////////")
            print("//////// TITULAR NO VÁLIDO. //////////////")
            print("//////////////////////////////////////////")
            print("")


    


 # %% EJECUTAR


def main():

    # EJERCICIO 8
    def ejercicio8():

        # Crear una persona enviando los valores de nombre, edad y dni
        titular = Persona("RitaLee",7,"23222222")

        # Crear una persona sin enviar valores
        #titular = Persona()

        # Crear un objeto CuentaJoven
        nueva_cuenta_joven = CuentaJoven(titular, 1000,80)

        # Muestra los datos de la cuenta joven creada
        nueva_cuenta_joven.mostrar()

        # Solicitud de retiro a partir del valor que ingresa el usuario
        print("SOLICITUD DE RETIRO")
        cantidad_retiro = int(input("Ingrese la cantidad a retirar de su cuenta: $"))
        nueva_cuenta_joven.retirar(cantidad_retiro)

        # Solicitud de ingreso a partir del valor que ingresa el usuario
        print("SOLICITUD DE INGRESO")
        cantidad_ingreso = int(input("Ingrese la cantidad a ingresar en su cuenta: $"))
        nueva_cuenta_joven.ingresar(cantidad_ingreso)

        # Muestra los datos de la cuenta
        nueva_cuenta_joven.mostrar()
        
       

    # Ejecuto el Ejercicio 8
    ejercicio8()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
