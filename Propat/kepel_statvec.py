'''
%  [statvec] = kepel_statvec (kepel)
%	The function kepel_statvec transforms the keplerian
%	elements kepel into the corresponding state vector in
%	the same reference system.
%
% Input:
%	kepel
% 		vector containing the keplerian elements:
%		(1) - semimajor axis of the orbit in meters.
%		(2) - eccentricity.
%		(3) - inclination in radians.
%		(4) - right ascension of ascending node in radians.
%		(5) - argument of perigee in radians.
%		(6) - mean anomaly in radians.
%
% Output:
%	statvec
%  		state vector in meters and meters/second.
%
% Authors:
%	Helio K. Kuga;
%	Valder M. Medeiros;
%	Valdemir Carrara		february/80		version 1.0
%	Valdemir Carrara		july 2005		(C version)
%   Valdemir Carrara            March/09        Matlab
'''

import math
import numpy as np
from rotmax import rotmax
from rotmaz import rotmaz
from rotmay import rotmay
from kepler import kepler

def kepel_statvec(kepel):

	np.set_printoptions(precision=4)

	EARTH_GRAVITY = 3.9860064e+14 #Earth's gravitational constant (m^3/s^2)

	a   = kepel[0] # Semi-major axis
	exc = kepel[1] # Eccentricity
	c1  = math.sqrt(1.0 - exc**2)

	# Rotation matrix
	orb2iner = (rotmaz(-kepel[3]).dot(rotmax(-kepel[2]))).dot(rotmaz(-kepel[4]))
	#print('orb2iner :\n{0}'.format(orb2iner))

	# Kepler's equation
	E = kepler(kepel[5], exc)

	sE = math.sin(E)
	cE = math.cos(E)
	c3 = (math.sqrt(EARTH_GRAVITY/a))/(1.0 - exc*cE)

	#print('sE : {0}'.format(sE))
	#print('cE : {0}'.format(cE))
	#print('c3 : {0:5E}'.format(c3))

	# State vector
	aux1 = np.array([ a*(cE - exc), a*c1*sE, 0])
	aux2 = np.array([-c3*sE, c1*c3*cE, 0])
	T1 = aux1.dot(orb2iner.T)
	T2 = aux2.dot(orb2iner.T)

	stat_vec = np.hstack((T1, T2))
	return stat_vec

if __name__ == "__main__":
	rad = math.pi/180.0
	kepel = np.array([ 7000000, 0.01, 98*rad, 0, 0, 0])
	stat = kepel_statvec(kepel)