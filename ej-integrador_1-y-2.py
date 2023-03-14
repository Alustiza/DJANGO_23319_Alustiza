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

# %% EJERCICIO 1
# Escribir una función que calcule el máximo común divisor entre dos números.


def maximo_comun_divisor(num1, num2):
    divisor = 1
    mcd = 1


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
    # mayor = max(num1, num2)
    # menor = min(num1, num2)
    mcm = (num1 * num2)//mcd #la doble barra de división devuelve un número entero
    return mcm

 # %% EJECUTAR


def main():

    # EJERCICIO 1
    def ejercicio1():
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
