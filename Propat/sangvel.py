'''
% [skew_ang_vel] = sangvel (w)
%   To obtain the skew simetric matrix of the satellite angular
%   velocity
%
% inputs:
%   w              - Satellite angular velocity (rd/s)
%
% outputs:
%   skew_ang_vel   - Angular velocity matrix (4 x 4)
% 

% Valdemir Carrara, Sep, 1998.
'''

import numpy as np

def sangvel(w):

	skew_ang_vel = np.array([ [0,      w[2], -w[1], w[0]],
							  [-w[2],     0,  w[0], w[1]],
							  [w[1],  -w[0],     0, w[2]],
							  [-w[0], -w[1], -w[2],    0] ])

	return skew_ang_vel

if __name__ == "__main__":
	print(sangvel(np.array([1,2,3,4])))
	print(sangvel(np.array([1,2,3,4])).shape)
