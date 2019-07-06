'''
% [rot_mat] = quatrmx (quaternion)
%   To compute the rotation matrix given the quaternions.
% inputs:
%   quaternion
%       attitude quaternions (4) Q = q1 i + q2 j + q3 k + q4
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Sep. 1998
'''
import numpy as np

def quatrmx(quaternion):

	q1q = quaternion[0]**2
	q2q = quaternion[1]**2
	q3q = quaternion[2]**2
	q4q = quaternion[3]**2

	q12 = 2*quaternion[0]*quaternion[1]
	q13 = 2*quaternion[0]*quaternion[2]
	q14 = 2*quaternion[0]*quaternion[3]
	q23 = 2*quaternion[1]*quaternion[2]
	q24 = 2*quaternion[1]*quaternion[3]
	q34 = 2*quaternion[2]*quaternion[3]

	rot_mat = np.array([ [(q1q - q2q - q3q + q4q), (q12 + q34), (q13 - q24)],
						 [(q12 - q34), (q2q + q4q - q1q - q3q), (q23 + q14)],
						 [(q13 + q24), (q23 - q14), (q3q + q4q - q1q - q2q)] ])

	return rot_mat


if __name__ == "__main__":
	A = np.array([1,2,3,4])
	B = np.array([1,1,1,1])
	C = np.array([1,0,1,0])
	print(quatrmx(C))