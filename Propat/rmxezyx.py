'''
% [euler_angles] = rmxezyx (rot_mat)
%   To compute the Euler angles of a Z-Y-X rotation, given 
%   the attitude matrix.
% inputs:
%   rot_mat
%       Rotation matrix (3, 3)
% outputs:
%   euler_angles
%       Euler angles from a Z-Y-X rotation, in radians (3)
%           -pi   < euler_angle(1) <= pi
%           -pi/2 < euler_angle(2) <= pi/2
%           -pi   < euler_angle(3) <= pi
%
% Valdemir Carrara, Feb, 2009
'''

import math
import numpy as np

def rmxezyx(rot_mat):

	np.set_printoptions(precision=4)

	stet = -rot_mat[0, 2]
	ctsf =  rot_mat[0, 1]
	ctcf =  rot_mat[0, 0]
	spct =  rot_mat[1, 2]
	cpct =  rot_mat[2, 2]

	if abs(stet) <= 1.0:
		eul2 = math.asin(stet)
	else:
		eul2 = (math.pi/2)*np.sign(stet)

	if (abs(eul2) <= (math.pi/2 - 1.0e-5)):

		#Caso 1
		if abs(ctcf) != 0:
			eul1 = math.atan2(ctsf, ctcf)
			if (eul1 > math.pi):
				eul1 = eul1 - 2*math.pi

		else:
			eul1 = (math.pi/2)*np.sign(ctsf)


		#Caso 2
		if abs(cpct) != 0:
			eul3 = math.atan2(spct, cpct)

			if(eul3 > math.pi):
				eul3 = eul3 - 2*math.pi
		else:
			eul3 = (math.pi/2)*np.sign(spct)

	else:
		
		capb = rot_mat[1, 1]
		sapb = rot_mat[1, 0]
		eul1 = 0.0

		if abs(capb) != 0:
			eul3 = math.atan2(sapb, capb)

			if(eul3 > math.pi):
				eul3 = eul3 - 2*math.pi
				print('eul3 : {0}'.format(eul3))
		else:
			eul3 = 0.0

	euler_angles = np.array([eul1, eul2, eul3])
	return euler_angles


if __name__ == "__main__":

	x = np.array([ [0.1, 0.2, 0.3], 
			       [0.5, 0.01, 0.2], 
				   [0.06, 0.05, 0.4] ])

	y = np.array([ [0.01, 0.03, 0.1], 
			       [0.05, 0.1, 0.2], 
				   [0.1, 0.04, 0.05] ])

	z = np.zeros((3,3))

	w = np.ones((3,3))*0.1

	print(rmxezyx(y.T))
