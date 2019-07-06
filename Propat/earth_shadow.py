'''
% [shadow] = earth_shadow (sat_pos, sun_pos)
%
%	The function earth_shadow verifies if a given position
%	is or isn't in the earth shadow.
%
% Inputs:
%	sat_pos
%		spacecraft coordinates in the inertial system, in meters.
%	sun_pos
%		coordinates of the sun in the inertial frame, in meters.
%
% Remarks:
%	1 - Earth is considered as a sphere
%	2 - Penunbra is calculated as straight horizon line
%
% Outputs:
%	earth_shadow
%		0: spacecraft is in the earth shadow
%		1: spacecraft is illuminated by the sun
%       between 0 and 1: spacecraft is in the Earth penumbra,
%		earth_shadow gives the visible fraction of the sun.
%
% Author:  Valdemir Carrara            mar/88        v. 1.0
%									july/05			C version
%   Valdemir Carrara            March/09 
'''

import math
import numpy as np

def earth_shadow(sat_pos, sun_pos):

	np.set_printoptions(precision=4)

	EARTH_RADIUS = 6378139.0 #Earth's radius in meters
	SUN_RADIUS   = 0.6953e+09 #Sun's radius (meters)

	dsun = np.linalg.norm(sun_pos)

	if dsun <= 0:
		shadow = -1 #A distância ao sol é nula

	else:
		#vecsun = sun_pos[0:2]/dsun -> Original
		vecsun = sun_pos/dsun
		rcob = np.dot(sat_pos, vecsun)
	
		#print('dsun   : {0}'.format(dsun))
		#print('vecsun : {0}'.format(vecsun))
		#print('rcob   : {0:.7}'.format(rcob))

		if rcob < 0:

			radi = SUN_RADIUS/dsun
			auxi = np.cross(sat_pos, vecsun)
			auxi = np.linalg.norm(auxi)
			psvs = ((auxi - EARTH_RADIUS)/rcob)/radi

			#print('radi : {0:4E}'.format(radi))
			#print('auxi : {0}'.format(auxi))
			#print('psvs   : {0}'.format(psvs))

			if abs(psvs) < 1:
				shadow = (math.acos(psvs)  \
						- psvs*math.sqrt(1.0 - psvs**2))/math.pi
				print('Shadow : {0:4E}'.format(shadow))

			else:

				if psvs >= 0:
					shadow = 0
				else:
					shadow = 1

		else:
			shadow = 1

	return shadow


if __name__ == "__main__":
	sat_pos = np.array([100,150,150])
	sun_pos = np.array([150,100,100])
	print(earth_shadow(sat_pos, sun_pos))