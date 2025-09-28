# adivina un numero, usando funciones

import numpy as np


def adivina_numero(number):
    """Funcion para adivinar un número función que hace el trabajo de interactuar
    con el usuario y evaluar si adivino el numero. 
    Entrada: number - entero, que el usuario no conoce

    salida: adivina - Numero de intenros para adivinar """
    intentos = 1

    numero_ingresado = int(input('adivine un numero: 1 al 999:'))

    while numero_ingresado != number:
        intentos = intentos + 1
        if (numero_ingresado > number):
            print(numero_ingresado, " es muy alto")
        elif (numero_ingresado < number):
            print(numero_ingresado, " es muy bajo")
        numero_ingresado = int(input("Adivine otra vez: "))
    return intentos

# Main program


# obtenga numero aleatorio [1, 1000]
rnum = np.random.randint(1, 1000)

# Llame a la funcion que interactua con usuario
nguess = adivina_numero(rnum)

print("\n Excelente, adivinaste en ", nguess, ' intentos')

