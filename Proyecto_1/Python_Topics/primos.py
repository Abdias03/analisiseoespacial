import numpy as np

maxnum = 100
prime = np.zeros(maxnum)
prime[0] = 1  # el 1 no es primo

maxi = int(np.floor(np.sqrt(maxnum)))
for ipos in range(1, maxi):
    if (prime[ipos] == 0):
        inum = ipos+1  # 2,3,4, ...
        maxj = int(np.floor(maxnum/inum))

        for j in range(2, maxj + 1):
            imult = inum*j  # x3, x3, x4
            prime[imult-1] = 1  # posicion, i-1
nprime = 0
for ipos in range(maxnum):
    if (prime[ipos] == 0):
        nprime += 1
        print(f'%4 {ipos+1}')

print("# primos encontrados ", nprime)
