'''
% [rot_mat] = rotmay (angle)
%   To obtain the rotation matrix around the Y axis given the
%   rotation angle.
% inputs:
%   angle
%       rotation angle, in radians.
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Sep, 1998
'''

import math
import numpy as np

def rotmay(angle):

	coan = math.cos(angle)
	sian = math.sin(angle)

	rot_mat = np.array([ [coan, 0, -sian],
						 [0   , 1,     0],
						 [sian, 0,  coan] ])

	return rot_mat

if __name__ == "__main__":

	print(rotmay(math.pi/4))
	print(rotmay(math.pi/3))
