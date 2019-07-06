'''
% [q_unit] = quat_unity (q)
%   To normalize the quaternion from a non-unity quaternion.
%   Normalization is based on euclidian norm:
%   q_unit = q/sqrt(q'*q);
%
% inputs:
%   q
%       Input quaternion (4)
%
% outputs:
%   q_unit
%       unity quaternion, such that:
%         q'*q = 1
% 
% Valdemir Carrara, May, 2015.
'''

import numpy as np
import math

def quat_unity(q):

	qnorm  = math.sqrt(np.dot(q, q.T))
	q_unit = np.zeros(4)

	if qnorm != 0:
		q_unit = q/qnorm
	else:
		q_unit[3] = 1

	return q_unit

if __name__ == "__main__":
	q = np.array([0,0,0,0])
	q = np.array([1,1,-1,-1])
	print(quat_unity(q))