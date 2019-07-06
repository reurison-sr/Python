'''
% [eccentric] = kepler (mean_anomaly, eccentricity)
%	The subroutine kepler finds a solution to the
%	kepler's equation.
%
% Input:
%	mean_anomaly
%		mean anomaly in radians.
%	eccentricity
%		eccentricity.
%
% Output:
%	eccentric
%		eccentric anomaly in radians.
%
% Authors:
%	Valder M. de Medeiros		june/81		version 2.0
%	Valdemir Carrara			july 2005	(C version)
%   Valdemir Carrara            March/09        Matlab
'''

import math
import numpy as np

def kepler(mean_anomaly, eccentricity):

	exc2  = eccentricity**2
	am1   = mean_anomaly % (2*math.pi)
	am2   = am1 * 2
	am3   = am1 + am2
	shoot =  am1 + eccentricity*(1.0 - 0.125*exc2)*math.sin(am1) \
	   + 0.5*exc2*(math.sin(am2) + 0.75*eccentricity*math.sin(am3))

	#print("exc2 : {0:.5}".format(exc2))
	#print("am1 : {0:.5}".format(am1))
	#print("am2 : {0:.5}".format(am2))
	#print("am3 : {0:.5}".format(am3))
	#print("shoot : {0:.5}".format(shoot))

	el = 1.0
	ic = 0

	while( (abs(el) > 1.0e-12) and (ic <= 10)):

		el =  (shoot - am1 - eccentricity*math.sin(shoot)) \
		     / (1.0 - eccentricity*math.cos(shoot))
		shoot = shoot - el
		ic    = ic + 1

	if (ic >= 10):
		print('warning ** subroutine kepler did not converge in 10 iterations')

	eccentric = shoot
	return eccentric

if __name__ == "__main__":
	rad = math.pi/180.0
	#kepel = np.array([7000000, 0.01, 98*rad, 0, 0, 0])
	#kepler(kepel[5], kepel[1])
	kepel = np.array([7000000, 0.01, 98*rad, 0, 0, 0.0167])
	kepler(kepel[5], kepel[1])

