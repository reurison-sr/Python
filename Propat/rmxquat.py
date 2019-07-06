'''
% [quaternions] = rmxquat (rot_mat)
%   To obtain the attitude quaternions from the attitude
%   rotation matrix.
% inputs:
%   rot_mat
%       rotation matrix (3, 3)
% outputs:
%   quaternion
%       attitude quaternions.
%

% Valdemir Carrara - Sep/1998
% Reurison Silva - April/2019 - Python Version
'''

import math
import numpy as np

def rmxquat(rot_mat):

	np.set_printoptions(precision=4)

	matra = np.trace(rot_mat)
	auxi  = 1 - matra
	selec = np.array([1 + matra, 
					  auxi + 2*rot_mat[0,0],
					  auxi + 2*rot_mat[1,1],
					  auxi + 2*rot_mat[2,2] ])

	auxi = np.max(selec)
	ites = np.argmax(selec)
	auxi = 0.5*math.sqrt(auxi)

	#print('select : {0}'.format(selec))
	#print('auxi : {0}'.format(auxi))
	#print('ites : {0}'.format(ites))
	
	div = 4*auxi

	if ites == 0:
		quaternions = np.array([ (rot_mat[1,2] - rot_mat[2,1])/div,
								 (rot_mat[2,0] - rot_mat[0,2])/div,
								 (rot_mat[0,1] - rot_mat[1,0])/div,
								 				auxi                 ])
	elif ites == 1:
		quaternions = np.array([ 				auxi,
							 	 (rot_mat[0, 1] + rot_mat[1, 0])/div,
							 	 (rot_mat[0, 2] + rot_mat[2, 0])/div, 
								 (rot_mat[1, 2] - rot_mat[2, 1])/div ])

	elif ites == 2:
		quaternions = np.array([ (rot_mat[0, 1] + rot_mat[1, 0])/div,
												auxi,
								 (rot_mat[1, 2] + rot_mat[2, 1])/div,
								 (rot_mat[2, 0] - rot_mat[0, 2])/div ])

	else:
		quaternions = np.array([ (rot_mat[0, 2] + rot_mat[2, 0])/div,
								 (rot_mat[1, 2] + rot_mat[2, 1])/div,
								  				auxi,
								 (rot_mat[0, 1] - rot_mat[1, 0])/div ])

	return quaternions

if __name__ == "__main__":
	A = np.array([ [1,2,3], [3,2,1], [1,0,1] ])
	B = np.array([ [0.1,11,2], [3,5,7], [13,0,1] ])
	print(rmxquat(B))