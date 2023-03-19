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

# %% EJERCICIO 3
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).



def crear_diccionario(txt1):
    '''
    Recibe una cadena de caracteres y devuelve un diccionario con cada palabra y la cantidad de veces que aparece.

    Args:
        txt1 (str): Cadena de caracteres de entrada.

    Returns:
        dict: Diccionario con las palabras contenidas en la cadena y la cantidad de veces que aparece cada una.

    '''
    txt1 = txt1.lower()
    lista_palabras = txt1.split()

    diccionario_cadena = {}
    for i in lista_palabras:
        if i in diccionario_cadena:
            diccionario_cadena[i] +=1
        else:
            diccionario_cadena[i]= 1

    return diccionario_cadena

# %% EJERCICIO 4
# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def mayor_frecuencia_diccionario(diccionario):
    '''
    Recibe un diccionario y devuelve la palabra más frecuente y su cantidad de apariciones.

    Args:
        diccionario (dict): Diccionario de entrada.

    Returns:
        tuple: Tupla con la palabra más frecuente y su cantidad de apariciones.

    '''
    palabra_mas_frecuente = ""
    cantidad=0
    for keys,values in diccionario.items():
        if values > cantidad:
            cantidad = values
            palabra_mas_frecuente = keys
    return palabra_mas_frecuente,cantidad





 # %% EJECUTAR


def main():
    '''
    
    Función principal que llama a las funciones "ejercicio3" y "ejercicio4".
    
    '''
    # EJERCICIO 3
    def ejercicio3():
        '''

        Pide una cadena de caracteres al usuario y devuelve un diccionario con cada palabra y la cantidad de veces que aparece.

        '''
        print("")
        print("Ejercicio 3")
        print("Ingrese una cadena de caracteres y le devolveremos un diccionario con cada palabra y la cantidad de veces que aparece:")
        print("")
        txt1 = (input("Ingrese una cadena de caracteres:"))
        resultado_ej3 = crear_diccionario(txt1)
        print("")
        print("La cadena de caracteres ingresada es:")
        print(txt1)
        print("")
        print("El resultado es un diccionario con las palabras contenidas en la cadena y la cantidad de veces que aparece cada una:")
        print("")
        print(resultado_ej3)
        print("El resultado es de tipo:", type(resultado_ej3))
        print("")
        print("")


    # EJERCICIO 4
    def ejercicio4():
        '''

        Pide una cadena de caracteres al usuario y devuelve la palabra más frecuente y su cantidad de apariciones.

        '''
        print("")
        print("Ejercicio 4")
        print("Ingrese una cadena de caracteres y le devolveremos cuál es la palabra que más aparece y cuántas veces lo hace:")
        print("")
        txt1 = (input("Ingrese una cadena de caracteres:"))
        resultado_ej4 = mayor_frecuencia_diccionario(crear_diccionario(txt1))
        print("")
        print("La cadena de caracteres ingresada es:")
        print(txt1)
        print("")
        print("El resultado es una tupla con la palabra más frecuente y su cantidad de apariciones:")
        print("")
        print(resultado_ej4)
        print("El resultado es de tipo:", type(resultado_ej4))

        print("")
        print("")


    # Ejecuto el Ejercicio 3
    ejercicio3()

    # Ejecuto el Ejercicio 4
    ejercicio4()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
