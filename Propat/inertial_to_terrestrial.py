'''
% [xterrestrial] = inertial_to_terrestrial (tesig, xi)
%	The function inertial_to_terrestrial transforms geocentric
%	inertial state vector into geocentric
%	terrestrial coordinates (referred to
%	Greenwich).
%
% Input:
%	tesig
%		Greenwich sidereal time in radians.
%	xi
%		geocentric inertial position vector.
%       (1) inertial geocentric position x (m)
%       (2) inertial geocentric position y (m)
%       (3) inertial geocentric position z (m)
%       (4) inertial geocentric velocity x (m/s)
%       (5) inertial geocentric velocity y (m/s)
%       (6) inertial geocentric velocity z (m/s)
%
% Output:
%	xterrestrial
%		corresponding geocentric terrestrial vector.
%
% Authors:
%	Helio/Valder/Valdemir-aug. 1981 - version 1.0
%	Helio		-july 1989 - version 1.1
%	Valdemir Carrara		july 2005		(C version)
%   Valdemir Carrara            March/09        Matlab
'''

import numpy as np
from rotmaz import rotmaz 

def inertial_to_terrestrial(tesig, xi):

	np.set_printoptions(precision=4)
	xt_aux = np.vstack((xi[0:3], xi[3:]))
	xterrestrial = np.dot(xt_aux, rotmaz(tesig).T)
	xterrestrial = np.hstack((xterrestrial[0], xterrestrial[1]))

	return xterrestrial

if __name__ == "__main__":
	xt = np.array([1,2,3,4,5,6])
	tesig = 0.5
	print(inertial_to_terrestrial(tesig, xt))

