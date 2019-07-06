''''
% [q_mat] = quat_matrix (q)
%   To obtain the quaterniom product matrix, such that
%   quat_matrix(Q)*P = quat_prod(Q, P)
%
% inputs:
%   q              - Input quaternion
%
% outputs:
%   q_mat          - Quaternion product matrix (4 x 4)
% 
% Valdemir Carrara, Jan, 2015.

'''


import numpy as np

def quat_matrix(q):

	q_mat = np.array([ [ q[3], -q[2],  q[1], q[0] ],
					   [ q[2],  q[3], -q[0], q[1] ],
					   [-q[1],  q[0],  q[3], q[2] ],
					   [-q[0], -q[1], -q[2], q[3] ] ])

	print(q_mat)


if __name__ == "__main__":
	q = np.array([1, 2, 3, 4])
	quat_matrix(q)
