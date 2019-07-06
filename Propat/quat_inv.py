'''

% [q_conj] = quat_inv (q)
%   To obtain the inverse quaternion of a given transform.
%   The inverse quaternion is equal to its conjugate
%   The inverse quaternion is such that quat_prod(q, q_conj)= [0 0 0 1]
%
% inputs:
%   q
%       Input quaternion (4)
%
% outputs:
%   q_conj
%       quaternion inverse, defined by:
%         [-q(1); -q(2); -q(3); q(4)]
% 
% Valdemir Carrara, Jan, 2015.

'''

import numpy as np

#Recebe 4x1

def quat_inv(q):

	q_conj = np.array([ -q[0],
						-q[1],
						-q[2],
						+q[3]  ])

	return q_conj

if __name__ == "__main__":
	p = np.array([ [1], [2], [3], [4] ])
	P = quat_inv(p)
	print(P)