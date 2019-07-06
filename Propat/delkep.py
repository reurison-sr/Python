"""
	Function delkep calculates the rate of
	variation of keplerian elements, considering only
	J2 and J4.

 Input:
	kep_el -> vector with the keplerian elements:
		(1) - semimajor axis of the orbit in meters.
		(2) - eccentricity.
		(3) - inclination in radians.
		(4) - right ascension of ascending node in radians.
		(5) - argument of perigee in radians.
		(6) - mean anomaly in radians.
       Obs: 4,5 and 6 are not used

 Output:
	deltakep
		(1) = 0
		(2) = 0
		(3) = 0
		(4) - variation rate of the right ascension of
		      ascending node, in radians/second.
		(5) - variation rate of the argument of perigee,
			  in radians/second.
		(6) - variation rate of the mean anomaly, in
			  radians/second.

Authors:
Valder M. de Medeiros  	September/81 	version 1.0
Valdemir Carrara 		July/05		    (C Version)
Valdemir Carrara        March/09           Matlab
Reurison Silva          April/19           Python
"""


import numpy as np
import math


def delkep(kep_el):

	#*kep_el -> vetor

	EARTH_RADIUS  = 6378139. # Earth's radius in meters
	EARTH_GRAVITY = 3.9860064e+14 #Earth's gravitational constant (m**3/s**2)
	J_2           =  1.0826268362e-3
	J_4           =  -1.62336e-6

	seix = kep_el[0]
	exce = kep_el[1]
	exc2 = exce**2 #exce**2
	eta2 = 1.0 - exc2
	eta1 = math.sqrt(eta2)
	teta = math.cos(kep_el[2])
	tet2 = teta**2
	tet4 = tet2**2
	aux0 = math.sqrt(EARTH_GRAVITY/(seix**3))
	plar = EARTH_RADIUS/(seix*eta2)
	pla2 = plar**2 
	gam2 = 0.5*J_2*pla2
	gam4 = -0.375*J_4*pla2**2

	#print('EARTH_RADIUS : {0}'.format(EARTH_RADIUS))
	#print('EARTH_GRAVITY : {:.7E}'.format(EARTH_GRAVITY))
	#print('J_2 : {:.2}'.format(J_2))
	#print('J_4 : {:.5E}'.format(J_4))
	#print('seix : {0}'.format(seix))
	#print('exce : {:.4}'.format(exce))
	#print('exc2 : {:.4}'.format(exc2))
	#print('eta2 : {:.4}'.format(eta2))
	#print('eta1 : {:.4}'.format(eta1))
	#print('teta : {:.4}'.format(teta))
	#print('tet2 : {:.4}'.format(tet2))
	#print('tet4 : {:.4}'.format(tet4))
	#print('aux0 : {:.4E}'.format(aux0))
	#print('plar : {:.4E}'.format(plar))
	#print('pla2 : {:.4E}'.format(pla2))
	#print('gam2 : {:.4E}'.format(gam2))
	#print('gam4 : {:.4E}'.format(gam4))

	deltakep = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	deltakep[3] = aux0*teta*(3.0*gam2*(-1.0
		+ 0.125*gam2*(9.0*eta2 + 12.0*eta1 - 5.0    \
		- (5.0*eta2 + 36.0*eta1 + 35.0)*tet2))      \
		+ 1.25*gam4*(5.0 - 3.0*eta2)*(3.0 - 7.0*tet2))

	deltakep[4] = aux0*(1.5*gam2*((5.0*tet2 - 1.0) +  \
	   + 0.0625*gam2*(25.0*eta2 + 24.0*eta1           \
	   - 35.0 + (90. - 192.0*eta1 - 126.0*eta2)*tet2  \
	   + (385.0 + 360.0*eta1 + 45.0*eta2)*tet4))      \
	   + 0.3125*gam4*(21.0 - 9.0*eta2 + (-270.0 + 126.0*eta2)*tet2 \
	   + (385.0 - 189.0*eta2)*tet4))

	deltakep[5] = aux0*(1.0 + eta1*(1.5*gam2*((3.0*tet2 - 1.0)  \
		+ 0.0625*gam2*(16.0*eta1 + 25.0*eta2 - 15.0        \
	    + (30.0 - 96.0*eta1 - 90.0*eta2)*tet2              \
	    + (105.0 + 144.0*eta1 + 25.0*eta2)*tet4))          \
	    + 0.9375*gam4*exc2*(3.0 - 30.0*tet2 + 35.0*tet4)))

	#print('deltakep[3] : {:.4E}'.format(deltakep[3]))
	#print('deltakep[4] : {:.4E}'.format(deltakep[4]))
	#print('deltakep[5] : {:.4E}'.format(deltakep[5]))

	return deltakep

if __name__ == "__main__":
	pass
	#delkep(1,0.1,3,1,2,3)
	#delkep(0.1,0.1,0.5,0.5,0.5,0.5)
	#delkep(0.01,0.01,0.05,0.05,0.05,0.05)