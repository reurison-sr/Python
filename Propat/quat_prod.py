'''
% [quaternion] = quat_prod (quat1, quat2)
%   To compute the product of two quaternions.
% inputs:
%   quat1
%       first quaternion (4) Q = q1 i + q2 j + q3 k + q4
%   quat2
%       second quaternion (4) P = p1 i + p2 j + p3 k + p4
% outputs:
%   quaternion
%       quaternion product (4) R = Q X P
%
% Obs:
%   The resulting quaternion is given equivalently by
%   quaternion = rmxquat(quatrmx(quat2)*quatrmx(quat1))
%   (see the transform sequence)

% Valdemir Carrara, Jan. 2015
'''

import numpy as np

def quat_prod(quat1, quat2):

	np.set_printoptions(precision=4)

	v1 = quat1[0:3]
	v2 = quat2[0:3]

	T1 = quat1[3]*v2 + quat2[3]*v1 + np.cross(v1, v2)
	T2 = quat1[3]*quat2[3] - np.dot(v1, v2)

	#print("v1 x v2 : {0}".format(C))
	#print("v1 . v2 : {0}".format(D))
	#print("T1      : {0}".format(T1))
	#print("T2      : {0}".format(T2))

	quaternion = np.hstack((T1, T2))
	print('quaternion : {0}'.format(quaternion))

if __name__ == "__main__":
	q1 = np.array([0.1,0.2,0.3,1])
	q2 = np.array([0.6,0.5,0.4,0.3])

	q3 = np.array([1,2,3,4])
	q4 = np.array([4,3,2,1])

	quat_prod(q3, q4) 