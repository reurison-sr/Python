'''
% [euler_angles] = rmxezxz (rot_mat)
%   To compute the Euler angles of a Z-X-Z rotation, given 
%   the attitude matrix.
% inputs:
%   rot_mat
%       matriz de rotação (3, 3)
% outputs:
%   euler_angles
%       Euler angles from a Z-X-Z rotation, in radians (3)
%       such that:
%           -pi   < euler_angle(1) <= pi
%           0    <= euler_angle(2) <=  pi
%           -pi   < euler_angle(3) <= pi
%

% Valdemir Carrara, Sep, 1998
'''

import math
import numpy as np

def rmxezxz(rot_mat):

	a11 = rot_mat[0, 0]
	a12 = rot_mat[0, 1]
	a13 = rot_mat[0, 2]
	a23 = rot_mat[1, 2]
	a31 = rot_mat[2, 0]
	a32 = rot_mat[2, 1]
	a33 = rot_mat[2, 2]

	if abs(a33) <= 1:
		eul2 = math.acos(a33)
	elif a33 < 0:
		eul2 = math.pi
	else:
		eul2 = 0.0

	if (abs(eul2) >= 0.00001):

		#Caso 1
		if a32 != 0:

			eul1 = math.atan2(a31, -a32)

		else:

			eul1 = (math.pi/2)*np.sign(a31)
			if (eul1 > math.pi):
				eul1 = eul1 - 2*math.pi

		#Caso 2
		if a23 != 0:

			eul3 = math.atan2(a13, a23)
			if (eul3 > math.pi):
				eul3 = eul3 - 2*math.pi

		else:
			eul3 = (math.pi/2)*np.sign(a13)

	else:

		eul1 = 0
		if a11 != 0:

			eul3 = math.atan2(a12, a11)

			if(eul3 > math.pi):
				eul3 = eul3 - 2*math.pi

		else:
			eul3 = (math.pi/2)*np.sign(a12)

	euler_angles = np.array([ eul1, eul2, eul3])
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

	print(rmxezxz(w))