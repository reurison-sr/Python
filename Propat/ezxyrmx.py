'''
% [rot_mat] = ezxyrmx (euler_angles)
%   To transform Euler angles from a Z-X-Y rotation 
%   into the rotation matrix.
% inputs:
%   euler_angles
%       Euler angles from a Z-X-Y rotation, in radians 
%       (3).
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Feb, 2009
'''

import numpy as np
from rotmax import rotmax
from rotmay import rotmay
from rotmaz import rotmaz

def ezxyrmx(euler_angles):

	np.set_printoptions(precision=4)

	T1 = rotmax(euler_angles[2])
	T2 = rotmay(euler_angles[1])
	T3 = rotmaz(euler_angles[0])
	rot_mat = (T1.dot(T2)).dot(T3)
	return rot_mat

if __name__ == "__main__":
	#euler_angles = np.array([0.5, 0.75, 0.25])
	euler_angles = np.array([0.15, 0.05, 0.55])
	print(ezxyrmx(euler_angles))