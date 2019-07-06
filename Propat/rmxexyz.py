'''
% [euler_angles] = rmxexyz (rot_mat)
%   To compute the Euler angles of a X-Y-Z rotation, given 
%   the attitude matrix.
% inputs:
%   rot_mat
%       rotation matrix (3, 3)
% outputs:
%   euler_angles
%       Euler angles from a X-Y-Z rotation, in radians (3)
%       such that:
%           -pi   < euler_angle(1) <= pi
%           -pi/2 < euler_angle(2) <= pi/2
%           -pi   < euler_angle(3) <= pi
% Valdemir Carrara, Sep, 1998

'''

import math
import numpy as np

def rmxexyz(rot_mat):

	np.set_printoptions(precision=4)

	a11 = rot_mat[0, 0]
	a12 = rot_mat[0, 1]
	a22 = rot_mat[1, 1]
	a21 = rot_mat[1, 0]
	a31 = rot_mat[2, 0]
	a32 = rot_mat[2, 1]
	a33 = rot_mat[2, 2]

	if abs(a31) <= 1:
		eul2 = math.asin(a31)
	elif a31 < 0:
		eul2 = -math.pi/2
	else:
		eul2 = math.pi/2

	if abs(a31) <= 0.99999:

		if a33 != 0:
			eul1 = math.atan2(-a32, a33)
			if (eul1 > math.pi):
				eul1 = eul1 - 2*math.pi
		else:
			eul1 = (math.pi/2)*np.sign(-a32)

		if a11 != 0:
			eul3 = math.atan2(-a21, a11)
			if (eul3 > math.pi):
				eul3 = eul3 - 2*math.pi
		else:
			eul3 = (math.pi/2)*np.sign(-a21)

	else:
		eul1 = 0
		if a22 != 0:
			eul3 = math.atan2(a12, a22)
			if (eul3 > math.pi):
				eule3 = eule3 - 2*math.pi
		else:
			eule3 = (math.pi/2)*sign(a12)

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
	print(rmxexyz(y.T))