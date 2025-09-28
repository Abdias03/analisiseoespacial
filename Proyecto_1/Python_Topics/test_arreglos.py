import numpy as np

# Genere tres arreglos
x = np.array([1, 2, 3])
y = np.ones(3)
z = np.ones(3)*2

# Imprima los tres arreglos
print('x = ', x)
print('y = ', y)
print('z = ', z)

# Asigne algunos valores
x[1] = 15
y[:] = 3
z = z - 1

# Imprima otra vez arreglos
print('')
print('x = ', x)
print('y = ', y)
print('z = ', z)
