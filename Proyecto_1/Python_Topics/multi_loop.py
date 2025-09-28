# Codigo para multiplicar dos numeros enteros,
# definidos por el usuario.
# Operacion se repite hasta que el usuario lo determine.
# Iteración definida

for i in range(1000):
    intxt = input('Digite dos enteros (0 0 stop) ')
    a, b = intxt.split()
    a = int(a)
    b = int(b)

    if (a == 0 and b == 0):
        break
    c = a*b
    print(a, "x", b, " = ", c)


# Operacion se repite con While loop.
# Iteración Indefinida

a = None
b = None
while (a != 0 or b != 0):
    intxt = input('Digite dos enteros (0 0  termina)')
    a, b = intxt.split()
    a = int(a)
    b = int(b)
    c = a*b
    print(a, "x", b, " = ", c)
