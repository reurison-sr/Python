'''
% [quaternions] = ezxzquat (euler_angles)
%   To transform Euler angles from a Z-X-Z rotation
%   into quaternions.
% inputs:
%   euler_angles
%       Euler angles from a Z-X-Z rotation, in radians 
%       (3).
% outputs:
%   quaternions
%       quaternions corresponding to the Euler angles 
%

% Valdemir Carrara, Sep 1998
'''

import numpy as np
from ezxzrmx import ezxzrmx
from rmxquat import rmxquat

def ezxzquat(euler_angles):

	rot_mat = ezxzrmx(euler_angles)
	#print('rot_mat : \n {0}'.format(rot_mat))
	quaternions = rmxquat(rot_mat)
	#print('quaternions : \n {0}'.format(quaternions))
	return quaternions

if __name__ == "__main__":
	#euler_angles = np.array([0.15, 0.05, 0.55])
	euler_angles = np.array([0.5, 0.75, 0.25])
	print(ezxzquat(euler_angles))