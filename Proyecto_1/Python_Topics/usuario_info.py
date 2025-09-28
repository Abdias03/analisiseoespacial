# codigo que solicita información del usuario
# y reporta los resultados

name = input("Cual es le nombre? ")
txt = input('Cual es su estatura (m)?')
altura = float(txt)
txt = input('Cuanto pesa Ud. (Kg)? ')
peso = float(txt)

print('%s, Ud. mide %4.2f m y pesa %5.1f kg' % (name, altura, peso))
