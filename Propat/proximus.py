'''
% [angle] = proximus (angleinp, angleprox)
%   returns with angleinp in the nearest position from
%   angleprox
% inputs:
%   angleinp
%       input angle, in radians
%   angleprox
%       given angle to compute variable angle in rad
% outputs:
%   angle
%       equals to angleinp, close to angleprox, in radians
%

% Valdemir Carrara, Oct. 1998
'''

import math

def proximus(angleinp, angleprox):

	test  = 2*math.pi
	angle = angleprox \
		    + (angleinp-angleprox+test/2) % test \
		    - test/2
	return angle

if __name__ == "__main__":
	angleinp = 1/4
	angleprox = 1/3
	print(proximus(angleinp, angleprox))