''' 
% [rot_mat] = rotmaz (angle)
%   To obtain the rotation matrix around the Z axis given the
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

def rotmaz(angle):

	coan = math.cos(angle)
	sian = math.sin(angle)
	rot_mat = np.array([ [ coan, sian, 0],
						 [-sian, coan, 0],
						 [   0,     0, 1] ])
	return rot_mat

if __name__ == "__main__":
	print(rotmaz(math.pi/4))
	print(rotmaz(math.pi/3))