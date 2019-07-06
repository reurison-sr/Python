'''
% [sunpos] = sun_dir (djm, ts)
%
%	The subroutine sun calculates the direction vector
%	(unit vector) of the Sun in the geocentric inertial system 
%
% Input:
%	djm
%		modified julian date in days, referred to 1950.0.
%	ts
%		fraction of the day in seconds.
%
% Output:
%	sunpos
%		direction vector of the sun:
%		(1) - direction of the sun (cosine) along x
%		(2) - direction of the sun (cosine) along y
%		(3) - direction of the sun (cosine) along z
%
% Remarks:
%   Valid for the range 2000-2050
%
% Author:
%	Helio Koiti Kuga            Fortran
%   Valdemir Carrara            Jan/2015        Matlab
'''

import math
import numpy as np

def sun_dir(djm, ts):

	np.set_printoptions(precision=4)

	idays = djm - 18261
	tttt  = idays + ts/86400

	# Orbit elements
	w   = 4.9382416 + 8.21936631e-7*tttt # [rad] or 282.9404 + 4.70935E-5*T [deg]
	m   = 6.2141924 + 0.01720197*tttt    # [rad] or 356.0470 + 0.9856002585*T [deg]
	m   = m % (2*math.pi)
	ecc = 0.016709 - 1.151E-9*tttt

	# Sun longitude (approximate true anomaly + perigee)
	u   = m + 2.0*ecc*math.sin(m) + w + 1.25*ecc**2*math.cos(m)
	ret = u
	su  = math.sin(u)

	#print('w : {:.4}'.format(w))
	#print('m : {:.4}'.format(m))
	#print('ecc : {:.4}'.format(ecc))
	#print('u : {:.4}'.format(u))
	#print('ret : {:.4}'.format(ret))
	#print('su : {:.4}'.format(su))

	# Ecliptic obliquity
	eps = 0.409093 - 6.2186081E-9*tttt # [rad] or 23.4393 - 3.563E-7*T [deg]
	print('eps : {:.4}'.format(eps))

	sun_pos = np.array([math.cos(u),
						su*math.cos(eps),
						su*math.sin(eps)])

	print('Sun pos : ', sun_pos)

if __name__ == "__main__":
	sun_dir(50000, 2000)
	sun_dir(80000, 3000)