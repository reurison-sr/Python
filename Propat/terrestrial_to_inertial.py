'''
% [xinert] = terrestrial_to_inertial (tesig, xt)
%	The function terrestrial_to_inertial transforms geocentric
%	terrestrial coordinates referred to Greenwich into
%	geocentric inertial coordinates.
%
% Input:
%	tesig
% 		Greenwich sidereal time in radians (See function gst).
%	xt
% 		geocentric terrestrial position vector.
%       (1) terrestrial geocentric position x (m)
%       (2) terrestrial geocentric position y (m)
%       (3) terrestrial geocentric position z (m)
%       (4) terrestrial geocentric velocity x (m/s)
%       (5) terrestrial geocentric velocity y (m/s)
%       (6) terrestrial geocentric velocity z (m/s)
%
% Output:
%	xinert
%		inertial geocentric state vector.
%
%Authors:
%	Helio/Valder/Valdemir-  Aug/1981  - version 1.0
%	Helio		            July/1989 - version 1.1
%	Valdemir Carrara		July/2005 - (C version)
%   Valdemir Carrara        March/09 
%   Reurison Silva 			April/19  - Python version
'''

from rotmaz import rotmaz
import numpy as np

def terrestrial_to_inertial(tesig, xt):

	#np.set_printoptions(precision=4)

	xt_aux = np.vstack((xt[0:3], xt[3:]))
	xinert = np.dot(xt_aux, rotmaz(-tesig).T)
	xinert = np.hstack((xinert[0], xinert[1]))
	return xinert


if __name__ == "__main__":
	xt = np.array([1,2,3,4,5,6])
	tesig = 0.5
	print(terrestrial_to_inertial(tesig, xt))
	