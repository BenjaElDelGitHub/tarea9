import math


def mostrar(numero):
    numero=math.floor(numero)
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")

def año(fecha):
    if fecha % 4 != 0:  # no divisible entre 4
        print("No es bisiesto")
    elif fecha % 4 == 0 and fecha % 100 != 0:  # divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 != 0:  # divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 == 0:  # divisible entre 4, 100 y 400
        print("Es bisiesto")

def total(numEntero):
    lista = [numEntero]
    for número in lista:
        suma = 0
        for dígito in str(número):
            suma += int(dígito)
        print(suma)