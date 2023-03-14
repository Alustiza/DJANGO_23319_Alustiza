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

# %% EJERCICIO 5
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int_recursiva():

    try:
        print("")
        valor_usr = int(input("Ingrese un valor numérico:"))
    except ValueError:

        print("Por favor ingresa SOLO NÚMEROS ENTEROS")
        get_int_recursiva()

    print("")
    print("El valor ingresado por el usuario es:", valor_usr)
    print("")
    


def get_int():

    valor_usr = ""
    print("")
    while type(valor_usr) != int:
        try:
            valor_usr = int(input("Ingrese un valor numérico:"))
        except ValueError:

            print("Por favor ingresa SOLO NÚMEROS ENTEROS")

        print("")
    
    print("El valor ingresado por el usuario es:", valor_usr)




 # %% EJECUTAR


def main():

    # EJERCICIO 5
    def ejercicio5():

        #get_int()
        get_int_recursiva()

    # Ejecuto el Ejercicio 5
    ejercicio5()


if __name__ == "__main__":
    main()
