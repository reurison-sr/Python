'''
% [geoc] = spherical_to_rectangular(spherical)
%	Function to transform rectangular terrestrial
%	geocentric coordinates in spherical coordinates
%	(longitude, geocentric latitude and distance).
%
% Inputs:
%	spherical
%		Geocentric coordinates vector:
%			1 = east longitude (rad)
%			2 = geocentric latitude (rad)
%			3 = geocentric distance (meters)
%
% Outputs:
%   geoc
%   		geocentric rectangular coordinates vector in meters
%           (1) geocentric position x (m)
%           (2) geocentric position y (m)
%           (3) geocentric position z (m)
%
% Authors:
%   Valdemir Carrara            May/09   
'''

import math
import numpy as np

def spherical_to_rectangular(spherical):

	clat = math.cos(spherical[1])
	geoc = np.array([ math.cos(spherical[0])*clat,
					  math.sin(spherical[0])*clat,
					  math.sin(spherical[1]) ])

	geoc = geoc * spherical[2]

	#print('{:4E}'.format(geoc[0]))
	#print('{:4E}'.format(geoc[1]))
	#print('{:4E}'.format(geoc[2]))

	return geoc

if __name__ == "__main__":
	retangular = np.array([100,100,100])
	spherical_to_rectangular(retangular)