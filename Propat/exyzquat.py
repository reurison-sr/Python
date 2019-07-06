'''
% [quaternions] = ezxzquat (euler_angles)
%   To transform Euler angles from a X-Y-Z rotation
%   into quaternions.
% inputs:
%   euler_angles
%       Euler angles from a X-Y-Z rotation, in radians (3)
% outputs:
%   quaternions
%       quaternions corresponding to the Euler angles 
%

% Valdemir Carrara, Sep 1998
'''

import numpy as np
from exyzrmx import exyzrmx
from rmxquat import rmxquat

def exyzquat(euler_angles):

	rot_mat = exyzrmx(euler_angles)
	quaternions = rmxquat(rot_mat)
	return quaternions

if __name__ == "__main__":
	#euler_angles = np.array([0.15, 0.05, 0.55])
	euler_angles = np.array([0.5, 0.75, 0.25])
	print(exyzquat(euler_angles))

