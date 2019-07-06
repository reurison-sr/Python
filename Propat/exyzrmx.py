'''
% [rot_mat] = exyzrmx (euler_angles)
%   To transform Euler angles from a X-Y-Z rotation 
%   into the rotation matrix.
% inputs:
%   euler_angles
%       Euler angles from a X-Y-Z rotation, in radians (3)
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Sep, 1998
'''

import numpy as np
from rotmax import rotmax
from rotmay import rotmay
from rotmaz import rotmaz

def exyzrmx(euler_angles):

	np.set_printoptions(precision=4)

	T1 = rotmaz(euler_angles[2])
	T2 = rotmay(euler_angles[1])
	T3 = rotmax(euler_angles[0])

	#print('T1 : \n {0}'.format(T1))
	#print('T2 : \n {0}'.format(T2))
	#print('T3 : \n {0}'.format(T3))

	rot_mat = (T1.dot(T2)).dot(T3)
	#print('rot_mat : \n{0}'.format(rot_mat))

	return rot_mat

if __name__ == "__main__":
	#euler_angles = np.array([0.5, 0.75, 0.25])
	euler_angles = np.array([0.15, 0.05, 0.55])
	print(exyzrmx(euler_angles))