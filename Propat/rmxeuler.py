'''
% [euler_angle, euler_vector] = rmxeuler (rot_mat)
%   To transform a rotation matrix into Euler angle and vector  
% inputs:
%   rot_mat
%       rotation matrix (3, 3)
% outputs:
%   euler_angle
%       Euler angle, in radians.
%   euler_vector
%       Euler_vector (3x1) (unity vector)
%
% Valdemir Carrara, Feb, 2008
'''

import math
import numpy as np

def rmxeuler(rot_mat):

	#np.set_printoptions(precision=4)

	trace = np.trace(rot_mat)

	if trace == 3:

		euler_angle = 0
		euler_vector = np.array([1, 0, 0])

	elif trace < -0.99999:

		euler_angle = math.pi
		w = np.array([rot_mat[0, 0],
					  rot_mat[1, 1],
					  rot_mat[2, 2]])
		euler_vector = np.sqrt((1 + w)/2) #Array

		#print('euler_angle :', euler_angle) #ok
		#print('w :', w) #ok
		#print('euler_vector :', euler_vector) #ok

		if euler_vector[0] > 0.5:

			euler_vector[1] = np.sign(rot_mat[0, 1])*euler_vector[1]
			euler_vector[2] = np.sign(rot_mat[2, 0])*euler_vector[2]

		elif euler_vector[1] > 0.5:

			euler_vector[0] = np.sign(rot_mat[0, 1])*euler_vector[0]
			euler_vector[2] = np.sign(rot_mat[1, 2])*euler_vector[2]

		else:

			euler_vector[0] = np.sign(rot_mat[2, 0])*euler_vector[0]
			euler_vector[1] = np.sign(rot_mat[1, 2])*euler_vector[1]

	else:

		euler_angle = math.acos((trace - 1) / 2)
		siang = math.sin(euler_angle)

		euler_vector = np.array([rot_mat[1, 2] - rot_mat[2, 1],
						         rot_mat[2, 0] - rot_mat[0, 2],
						         rot_mat[0, 1] - rot_mat[1, 0]])

		euler_vector = euler_vector / (2*siang)

	#print('euler_angle : ',euler_angle)
	#print('euler_vector : ',euler_vector)

	return (euler_angle, euler_vector)

if __name__ == "__main__":
	A = np.array([ [.1,2,.3], [.3,.5,.1], [.251,0.8,0.57] ])
	print(rmxeuler(A))
