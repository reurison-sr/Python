'''
% [q_norm] = quat_norm (q)
%   To normalize the quaternion from a non-unity quaternion.
%   The scalar component (q4) remains unchanged.
%
% inputs:
%   q
%       Input quaternion (4)
%
% outputs:
%   q_unit
%       unity quaternion, such that:
%         q*q' = 1
% 
% Valdemir Carrara, May, 2015.
'''

import math
import numpy as np

# q = i*q1 + j*q2 + k*q3 + q4
#No matlab : [1;2;3;4]

def quat_norm (q):

	np.set_printoptions(precision=4)

	v = q[0:3]
	e = q[3]

	if (e > 1):
		e = 1
	if (e < -1):
		e = -1

	vnorm = np.dot(v.T, v)
	enorm = e**2

	#print('vnorm : {0}'.format(vnorm))
	#print('enorm : {0}'.format(enorm))

	if vnorm != 0:
		enorm = math.sqrt((1 - enorm)/vnorm)
		q_norm = np.hstack((enorm*v, e))
	else:
		q_norm = np.array([0, 0, 0, 1])

	#print(q_norm)

	return q_norm

if __name__ == "__main__":
	A = np.array([1,2,3,4])
	B = np.array([1,2,3,-4])
	C = np.array([-1/2,-1/5,0.77,-0.988])
	quat_norm(C)
