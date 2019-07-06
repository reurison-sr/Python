'''
% [spherical] = rectangular_to_spherical (geoc)
%	Function to transform rectangular terrestrial
%	geocentric coordinates in spherical coordinates
%	(longitude, geocentric latitude and distance).
%
% Inputs:
%   geoc
%   		geocentric rectangular coordinates vector in meters
%           (1) geocentric position x (m)
%           (2) geocentric position y (m)
%           (3) geocentric position z (m)
%
% Outputs:
%	spherical
%		Geocentric coordinates vector:
%			1 = east longitude (rad)
%			2 = geocentric latitude (rad)
%			3 = geocentric distance (meters)
%
% Authors:
%   Valdemir Carrara            May/09   
'''

import math
import numpy as np

def rectangular_to_spherical(geoc):

	np.set_printoptions(precision=4)

	px = geoc[0]
	py = geoc[1]
	pz = geoc[2]
	ws = px**2 + py**2
	rw = math.sqrt(ws + pz**2)
	lg = math.atan2(py, px)
	lt = math.atan2(pz, math.sqrt(ws))
	spherical = np.array([lg, lt, rw])

	return spherical

if __name__ == "__main__":
	#geoc = np.array([1000, 1500, 2000])
	geoc = np.array([3500, 2750, 1111])
	print(rectangular_to_spherical(geoc))