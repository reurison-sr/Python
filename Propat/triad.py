'''
% [c_triad] = triad(v, w)
% purpose:
%   To calculate the attitude matrix from a frame in which a pair of 
%   non aligned vectors v and w are known, to reference system such that 
%   the x axis is aligned to v, the y axis lies in the v-w plane and z is
%   orthogonal to the v-w plane. If v is aligned to w then a identity 
%   matrix is returned.
% inputs:
%   v, w
%       Body vectors v and w (3x1)
%
% Valdemir Carrara, April, 2015
%
'''

import numpy as np

def triad(v, w):

	np.set_printoptions(precision=4)

	nz = np.linalg.norm(v)
	if (nz == 0):
		c_triad = np.eye(3)
	else:
		x = v/np.linalg.norm(v)
		z = np.cross(x, w)
		z = z/np.linalg.norm(z) #Vetor unitário Z
		y = np.cross(z, x)
		c_triad = np.hstack((np.hstack((x, y)), z))

	return c_triad
		
if __name__ == "__main__":
	v = np.array([1,2,3])
	w = np.array([3,2,1])
	triad(v, w)
	