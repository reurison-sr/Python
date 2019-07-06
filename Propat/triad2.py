'''
% [c_triad] = triad(vb, wb, vr, wr)
% purpose:
%   To calculate the rotation matrix (attitude) from two pairs of given 
%   vectors, known in two different reference frames, using the TRIAD 
%   algorithm.
% inputs:
%   vb, wb
%       Body vectors v and w (3x1)
%   vr, wr
%       Reference vectors v and w (3x1)
%
% output
%   c_triad
%       Transformation matrix: u_b = c_triad * u_r
%       c_triad = c_b_r
%
% Valdemir Carrara, Oct, 2012
'''

import numpy as np
from triad import triad



def triad2(vb, wb, vr, wr): 

	c_triad = np.dot(triad(vb, wb).T, triad(vr, wr))
	return c_triad

if __name__ == "__main__":
	a = np.array([1,0,0])
	b = np.array([0,1,0])
	c = np.array([1,3,5])
	d = np.array([5,1,7])
	print('{:.4}'.format(triad2(a, b, c, d)))