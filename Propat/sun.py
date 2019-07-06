'''
% [sunpos] = sun (djm, ts)
%
%	The subroutine sun calculates the position vector
%	of the Sun in the geocentric inertial system refered
%	to j2000 equator and equinox.
%
% Input:
%	djm
%		modified julian date in days, referred to 1950.0.
%	ts
%		fraction of the day in seconds.
%
% Output:
%	sunpos
%		position vector of the sun:
%		(1) - first component of earth-sun position vector in meters.
%		(2) - second component of earth-sun position vector in meters.
%		(3) - third component of earth-sun position vector in meters.
%		(4) - right ascension in radians.
%		(5) - declination in radians.
%		(6) - radius vector (distance) in meters.
%
% Remarks:
%	this subroutine is optimized from 1950-1-1 00:01:06
%	until year 2050.
%
% Author:
%	Helio Koiti Kuga and Ulisses T. V. Guedes * version 1.0
%	C version by Valdemir Carrara 7/05
%   Valdemir Carrara            March/09        Matlab
'''

import math
import numpy as np

def sun(djm, ts):

	#np.set_printoptions(precision=4) #print options to numpy

	rad = math.pi/180.0
	ASTRONOMICAL_UNIT = 149.60e+09 # Astronomical unit (meters)

	t = djm - 18262.5 + ts/86400.0

	#Long. media do sol, corrigida
	alom_ab = (280.460 + 0.9856474*t)*rad % (2*math.pi)

	if alom_ab < 0:
		alom_ab = alom_ab + 2*math.pi

	#print('t : {:.4}'.format(t))
	#print('alom_ab : {:.4}'.format(alom_ab))

	# Anomalia média
	an_mean = (357.528 + 0.9856003*t)*rad % (2*math.pi)
	if an_mean < 0:
		an_mean = an_mean + 2*math.pi

	an_mean_2 = an_mean * 2

	if an_mean_2 > 2*math.pi:
		an_mean_2 = (an_mean_2) % (2*math.pi)

	#print('an_mean : {:.4}'.format(an_mean))
	#print('an_mean_2 : {:.4}'.format(an_mean_2))

	ecli_lo = alom_ab + (1.915*math.sin(an_mean) \
			  +0.02*math.sin(an_mean_2))*rad
	sin_ecli_lo = math.sin(ecli_lo)
	cos_ecli_lo = math.cos(ecli_lo)

	#print('ecli_lo : {:.4}'.format(ecli_lo))
	#print('sin_ecli_lo : {:.4}'.format(sin_ecli_lo))
	#print('cos_ecli_lo : {:.4}'.format(cos_ecli_lo))

	# ecliptic latitude	ecli_la = 0

	obl_ecli = (23.439 - 4.0e-7*t)*rad
	sin_obl_ecli = math.sin(obl_ecli)
	cos_obl_ecli = math.cos(obl_ecli)

	#print('obl_ecli : {:.4}'.format(obl_ecli))
	#print('sin_obl_ecli : {:.4}'.format(sin_obl_ecli))
	#print('cos_obl_ecli : {:.4}'.format(cos_obl_ecli))

	sunpos = np.zeros(6)
	
	sunpos[3] = math.atan2(cos_obl_ecli*sin_ecli_lo, cos_ecli_lo)
	if sunpos[3] < 0:
		sunpos[3] = sunpos[3] + 2*math.pi

	sunpos[4] = math.asin(sin_obl_ecli*sin_ecli_lo)
	sunpos[5] = (1.00014 - 0.01671*math.cos(an_mean) \
		       - 1.4e-4*math.cos(an_mean_2))*ASTRONOMICAL_UNIT
	sunpos[0] = sunpos[5] * cos_ecli_lo
	sunpos[1] = sunpos[5] * cos_obl_ecli * sin_ecli_lo
	sunpos[2] = sunpos[5] * sin_obl_ecli * sin_ecli_lo

	return sunpos


if __name__ == "__main__":
	print(sun(10000, 3600))
	print(sun(50000, 2200))