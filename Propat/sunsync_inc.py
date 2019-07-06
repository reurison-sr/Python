'''
%
%   sunsync_inclination = sunsync_inc (sma, exc)
%   This routine calculates the sunsynchronous inclination or a given 
%   orbit
%
%   Input:
%       sma  
%           Orbit semi-major axis (m)
%       exc
%           Orbit eccentricity
%
%   Output:
%     sunsync_inclination
%           Sun-Synchronous inclination of the orbit (rad).
%
%   Author:
%       Valder Matos de Medeiros        15/05/1987  Fortran version
%       Valdemir Carrara                May/2017    Matlab version
%

'''

import math
import numpy as np
from delkep import delkep

def sunsync_inc(sma, exc):

	np.set_printoptions(precision=4)

	earth_gravity   = 3.9860064e+14 # Earth's gravity (m^3/s^2)
	tropic_year     = 365.24219879	# Tropical year (days)
	earth_radius	= 6378139.0     # Earth's radius in meters
	arg     = 1.72     # First approximated inclination
	j_2     = 1.0826268362e-3 # J2 = 484.16544e-6 * SQRT(5.e0)
	el      = np.array([sma, exc, arg, 0, 0, 0]) # keplerian elements

	omegap  = (2*math.pi/tropic_year)/86400  # rate of the ascending node
	amm     = math.sqrt(earth_gravity/(sma**3)); # mean mean motion
	con     = (-1.5*j_2*amm*earth_radius**2)/(sma**2)
	del_    = 1
	ic      = 0

	#print('omegap : {:.4}'.format(omegap))
	#print('amm    : {:.4}'.format(amm))
	#print('con    : {:.4}'.format(con))
	#print('del_   : {0}'.format(del_))
	#print('ic     : {0}'.format(ic))

	while (abs(del_)  > 1e-6 and ic < 20):

		delk = delkep(el)
		chu  = math.cos(arg)
		del_ = (omegap - delk[3])/con
		chu = chu + del_
		arg = math.acos(chu)
		el[2] = arg
		ic += 1

	if (ic > 20):
		print('''Error in function sunsync_inclination: 
			  Interaction did not converge''')
		return None
	else:
		sunsync_inclination = arg
		return sunsync_inclination


	#print('sunsync_inclination : {:.5}'.format(sunsync_inclination))

if __name__ == "__main__":
	print(sunsync_inc(600000, 0.0167))
	print(sunsync_inc(400000, 0.02))

