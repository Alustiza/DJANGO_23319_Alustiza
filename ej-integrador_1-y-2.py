#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# < ^ >  { }  [ ] ' ' [' ']
"""
CODO A CODO: DJANGO
AÑO: 2023
COMISIÓN: 23319
@author: pabloalustiza

ACTIVIDAD DE INTEGRACIÓN 

Este programa incluye dos funciones:
ejercicio1() : para calcular el máximo común divisor (MCD) entre dos números.
ejercicio2() : para calcular el mínimo común múltiplo (MCM) entre dos números.

"""

# %% EJERCICIO 1
# Escribir una función que calcule el máximo común divisor entre dos números.


def maximo_comun_divisor(num1, num2):
    """
    Calcula el máximo común divisor (MCD) entre dos números.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.

    Returns:
        int: El máximo común divisor entre num1 y num2.
    """

    # Verificar si uno de los números es cero
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    divisor = int(1)
    mcd = int(1)

    mayor = max(num1, num2)
    menor = min(num1, num2)

    while (divisor <= menor):
        if (mayor % divisor == 0 and menor % divisor == 0):
            mcd = mcd*divisor
            mayor = mayor//divisor
            menor = menor//divisor
            divisor = 1

        divisor = divisor+1

    return mcd


# %% EJERCICIO 2
# Escribir una función que calcule el mínimo común múltiplo entre dos números

def minimo_comun_multiplo(num1, num2, mcd):
    """
    Calcula el mínimo común múltiplo (MCM) entre dos números.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.
        mcd (int): Máximo común divisor entre num1 y num2.

    Returns:
        int: El mínimo común múltiplo entre num1 y num2.

    """
     
    # mayor = max(num1, num2)
    # menor = min(num1, num2)
    # la doble barra de división devuelve un número entero
    mcm = (num1 * num2)//mcd
    return mcm

 # %% EJECUTAR


def main():
    """
    Función principal que ejecuta los ejercicios 1 y 2.
    """

    # EJERCICIO 1
    def ejercicio1():
        """
        Ejercicio 1: Calcula el Máximo Común Divisor (MCD) entre dos números.
        """
        print("")
        print("Calcula el Máximo Común Divisor (MCD) entre dos números:")
        print("")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado_ej1 = maximo_comun_divisor(num1, num2)
        print("")
        print("El MCD entre", num1, "y", num2, "es:", resultado_ej1)
        print("")
        print("")

    # EJERCICIO 2
    def ejercicio2():
        """
        Ejercicio 2: Calcula el Mínimo Común Múltiplo (MCM) entre dos números.
        """

        print("")
        print("Calcula el Mínimo Común Múltiplo (MCM) entre dos números:")
        print("")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        mcd = maximo_comun_divisor(num1, num2)
        resultado_ej2 = minimo_comun_multiplo(num1, num2, mcd)
        print("")
        print("El MCM entre", num1, "y", num2, "es:", resultado_ej2)
        print("")
        print("")

    # Ejecuto el Ejercicio 1
    ejercicio1()

    # Ejecuto el Ejercicio 2
    ejercicio2()


if __name__ == "__main__":
    main()
