# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:05:20 2019

% [rot_mat] = eulerrmx (euler_angle, euler_vector)
%   To transform Euler angle and vector  
%   into the rotation matrix.
% inputs:
%   euler_angle
%       Euler angle, in radians.
%   euler_vector
%       Euler_vector (3x1) (unity vector)
% outputs:
%   rot_mat
%       rotation matrix (3, 3)
%

% Valdemir Carrara, Feb, 2008
"""

import math
import numpy as np
from cross_matrix import cross_matrix

def eulerrmx(euler_angle, euler_vector):
    
    coan = math.cos(euler_angle)
    sian = math.sin(euler_angle)
    com1 = 1.0 - coan

    rot_mat = np.zeros((3, 3))
    
    #a = coan*np.eye(3);
    #b = com1*np.dot(euler_vector, euler_vector.T)
    #c = sian*cross_matrix(euler_vector)
    #print('a :', a)
    #print('------------------')
    #print('b :', b)
    #print('------------------')
    #print('c :', c)
    #print('-------------------')
    #print('a + b - c: ', a + b - c)

    rot_mat = coan*np.eye(3) \
            + com1*np.dot(euler_vector,euler_vector.T) \
            - sian*cross_matrix(euler_vector)
            
    return rot_mat

if __name__ == "__main__":
	print(eulerrmx(math.pi/3, np.array([ 0, 1, 0])))
