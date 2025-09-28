# MCD con una función

"""Cree la definición para calcular el MCD"""


def gcf(a, b):
    amin = min(a, b)
    mcd = 1
    for j in range(2, amin+1):
        if (a % j == 0 and b % j == 0):
            mcd = j
    return mcd


# Ahora, el programa principal
for i in range(10):
    intxt = input('Digite dos enteros (0 0  para terminar)')
    a, b = intxt.split()
    a = int(a)
    b = int(b)
    if (a == 0 and b == 0):
        break
    mcd = gcf(a, b)  # debe crear la función

    print("Maximo común divisor = ", mcd)
