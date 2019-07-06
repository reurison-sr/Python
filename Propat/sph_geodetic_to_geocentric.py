'''
% [geoc] = sph_geodetic_to_geocentric (spgd)
%
%	Function to transform spherical geodetic coordinates
%	(longitude, latitude and altitude) in rectangular
%	terrestrial geocentric coordinates
%
% Inputs:
%	spgd
%		Geodetic coordinates
%			(1) east longitude (rad)
%			(2) geodetic latitude (rad)
%			(3) geodetic altitude (meters)
%
% Outputs:
%   sph_geodetic_to_geocentric
%   		geocentric rectangular coordinates in meters
%           (1) geocentric position x (m)
%           (2) geocentric position y (m)
%           (3) geocentric position z (m)
%
% Authors:
%	Helio K. Kuga	    08/83   V. 1.0
%	Valdemir Carrara	08/05	C version
%   Valdemir Carrara    03/09   
%   Reurison Silva      04/19   Python Version    
'''

import math
import numpy as np

def sph_geodetic_to_geocentric(spgd):

	EARTH_FLATNESS	= 0.0033528131778969144 #Flattening factor = 1./298.257
	EARTH_RADIUS	= 6378139.0				# Earth's radius in meters

	al = spgd[0] # east longitude
	h  = spgd[2] # heigth
	sf = math.sin(spgd[1]) #geodetic latitude
	cf = math.cos(spgd[1])
	gama = (1.0 - EARTH_FLATNESS)
	gama = gama**2
	s = EARTH_RADIUS / math.sqrt(1.0 - (1.0 - gama)*sf**2)
	gl = (s + h) * cf

	geoc = np.array([gl*math.cos(al), 
					 gl*math.sin(al),
					 (s*gama + h)*sf ])

	#print('{:4E}'.format(geoc[0]))
	#print('{:4E}'.format(geoc[1]))
	#print('{:4E}'.format(geoc[2]))

	return geoc

if __name__ == "__main__":
	sph_geodetic_to_geocentric(np.array([100,1000,100]))