"""En algunos casos, se requiere de funciones que puedan regresar multiples variable 
    como resultado. En python la misma función puede retornar distintas variables como resultados"""

# Calcula la distancia y azimut entre dos puntos sobre una esfera.


def sph_azi(flat1, flon1, flat2, flon2):
    """
    SPH_AZI computes distance and azimuth between 2 points on the sphere 

    Intputs: flat1 = latitude of first point (degress)
    flon2 = longitude of first point (degrees)
    flat2 = lantitude of second point (degrees)
    flon2 = longitude of second point (degrees)

    returns: del = angular separation (degrees)
             azi = azimuth from 1 to 2, from N (deg.)

    Notes:
    (1) applies to geocentric not geographic lat,lon on Earth 
    (2) this routine is accurate depending on the precision of the real numbers used. python 
    should be accurate to real(8) precision. For greater accuracy, perform a separate calculation
    for close ranges using Cartesian geometry. 
    """
    # importe modulos necesarios
    import math as mt
    import numpy as np

    if ((flat1 == flat2 and flon1 == flon2) or (flat1 == 90. and flat2 == 90.) or (flat1 == -90. and flat2 == -90.)):
        delta = 0.
        azi = 0.
        return [delta, azi]

    # Perform calculation
    delta = 0.
    azi = 0.

    raddeg = mt.pi/180.

    theta1 = (90.-flat1)*raddeg
    theta2 = (90.-flat2)*raddeg

    phi1 = flon1*raddeg
    phi2 = flon2*raddeg

    stheta1 = mt.sin(theta1)
    stheta2 = mt.sin(theta2)
    ctheta1 = mt.cos(theta1)
    ctheta2 = mt.cos(theta2)

    cang = stheta1*stheta2*mt.cos(phi2-phi1)+ctheta1*ctheta2
    ang = mt.acos(cang)
    delta = ang/raddeg

    sang = mt.sqrt(1.-cang*cang)
    caz = (ctheta2-ctheta1*cang)/(sang*stheta1)
    saz = -stheta2*mt.sin(phi1-phi2)/sang
    az = mt.atan2(saz, caz)
    azi = az/raddeg
    if (azi < 0.):
        azi = azi+360.
    return [delta, azi]

# Programa principal


lat1 = None
lon1 = None
lat2 = None
lon2 = None

while (lat1 != 0. or lon1 != 0. or lat2 != 0. or log2 != 0.):
    intxt = input('Digite lat/lon del primer punto  ')
    lat1, lon1 = intxt.split()
    lat1 = float(lat1)
    lon1 = float(lon1)

    intxt = input('Digite lat/lon del segundo punto  ')
    lat2, lon2 = intxt.split()
    lat2 = float(lat2)
    lon2 = float(lon2)

    delta, azi = sph_azi(lat1, lon1, lat2, lon2)
    # print('Distancia y acimut: %6.2f %7.2f' % (delta, azi))
    print(f'Distancia y acimut: {delta:6.2f}{azi:7.2f}')
