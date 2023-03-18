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
Se utiliza para limpiar la pantalla antes de ejecutar main()
"""

# %% EJERCICIO 5
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.


def get_int_recursiva():
    """
    
    Función recursiva que solicita al usuario un valor entero hasta que se ingresa uno válido.

    Returns:
    int: el valor entero ingresado por el usuario.

    """
    print("RESOLUCIÓN RECURSIVA")
    try:
        valor_usr = int(input("Ingrese un valor numérico:"))
        print("Ingresaste correctamente el número:", valor_usr, type(valor_usr))
        print("")
        return valor_usr
    except ValueError:
        print("Por favor ingresa SOLO NÚMEROS ENTEROS")
        return get_int_recursiva()


def get_int_iterativa():
    """

    Función iterativa que solicita al usuario un valor entero hasta que se ingresa uno válido.

    Returns:
    int: el valor entero ingresado por el usuario.

    """
    print("RESOLUCIÓN ITERATIVA")
    while True:
        try:
            valor_usr = int(input("Ingrese un valor numérico:"))
            print("Ingresaste correctamente el número:",
                  valor_usr, type(valor_usr))
            print("")
            return valor_usr
        except ValueError:
            print("Por favor ingresa SOLO NÚMEROS ENTEROS")

 # %% EJECUTAR


def main():
    """

    Función principal que ejecuta el programa en sus dos resoluciones: recursiva e iterativa

    """
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ejecuto el Ejercicio 5 /// Resolución recursiva
    get_int_recursiva()

    # Ejecuto el Ejercicio 5 /// Resolución iterativa
    get_int_iterativa()


if __name__ == "__main__":
    main()
