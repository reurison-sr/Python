'''
% [rot_mat] = ezxzrmx (euler_angles)
%   To transform Euler angles from a Z-X-Z rotation 
%   into the rotation matrix.
% inputs:
%   euler_angles
%       Euler angles from a Z-X-Z rotation, in radians 
%       (3).
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Sep, 1998

'''

import numpy as np
from rotmax import rotmax
from rotmaz import rotmaz

def ezxzrmx(euler_angles):

	np.set_printoptions(precision=4)

	T1 = rotmaz(euler_angles[2])
	T2 = rotmax(euler_angles[1])
	T3 = rotmaz(euler_angles[0])
	rot_mat = (T1.dot(T2)).dot(T3)
	return rot_mat

if __name__ == "__main__":
	#euler_angles = np.array([0.5, 0.75, 0.25])
	euler_angles = np.array([0.15, 0.05, 0.55])
	print(ezxzrmx(euler_angles))