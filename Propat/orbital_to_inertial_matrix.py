'''
%  [rmx_i_o] = orbital_to_inertial_matrix (kepel)
%	The function orbital_to_inertial_matrix computes the rotation matrix
%	from orbital frame to inertial frame
%   The orbital frame is define as:
%      x_o : along the radius vector, from Earth center to satellite,
%            positive up
%      y_o : close to the velocity vector, but orthogonal to x_o, in
%            the orbital plane
%      z_o : normal to the orbital plane, along the orbital angular
%            momentum
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
%	rmx_i_o
%  		rotation matrix from orbital to inertial frame
%       r_inertial = rmx_i_o * r_orbital
%
% Authors:
%   Valdemir Carrara            Feb/12        Matlab
'''

import math
import numpy as np
from rotmax import rotmax
from rotmaz import rotmaz
from kepler import kepler

def orbital_to_inertial_matrix(kepel):

	np.set_printoptions(precision=4)

	exc = kepel[1] # Eccentricity
	c1  = math.sqrt(1.0 - exc**2)

	# Rotation matrix from perigee to inertial
	orb2iner = (rotmaz(-kepel[3]).dot(rotmax(-kepel[2]))).dot(rotmaz(-kepel[4]))

	#print("exc : {0:.4}".format(exc))
	#print("c1  : {0:.4}".format(c1))
	#print("orb2iner : \n{0}".format(orb2iner))

	# Kepler's equation
	E = kepler(kepel[5], exc) #Excentric anomaly
	sE = math.sin(E)
	cE = math.cos(E)
	r_ov_a = 1.0 - exc*cE
	cf     = (cE - exc)/r_ov_a # cosine of the true anomaly
	sf     = c1*sE/r_ov_a # sine of the true anomaly

	#print("r_ov_a : {0}".format(r_ov_a))
	#print("cf : {0:.4}".format(cf))
	#print("sf  : {0:.4}".format(sf))

	rmx_i_o = np.array([ [cf, sf, 0],
						 [sf, cf, 0],
						 [0,   0, 1] ])

	rmx_i_o = orb2iner.dot(rmx_i_o)
	#print('rmx_i_o : {0}'.format(rmx_i_o))

	return rmx_i_o


if __name__ == "__main__":
	rad = math.pi/180.0
	kepel = np.array([ 7000000, 0.01, 98*rad, 0, 0, 0])
	print(orbital_to_inertial_matrix(kepel))