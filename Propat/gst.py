'''
% [gwst] = gst (diju, time)
%   The function gst furnishes the greenwich aparent mean 
%   sidereal time referred to the J2000.0 equator and equinox.
% inputs:
%   diju
%       Modified Julian Date in days, referred to 1950.0.
%   time
%       UT1 time complement in seconds.
% outputs:
%   gwst
%       Greenwich aparent sidereal time in radians
%
% Valdemir Carrara, Apr, 2003
'''

import math

def gst(diju, time):

	tsj  = (diju - 18262.5)/36525;
	tsgo = (24110.54841 + (8640184.812866 \
		 + 9.3104e-2*tsj - 6.2e-6*tsj*tsj)*tsj)*math.pi/43200
	tetp = 7.292116e-5 #velocidade angular da Terra (rd/s)
	gwst = (tsgo + time*tetp) % (2*math.pi)
	
	return gwst

if __name__ == "__main__":
	print('{:1.4}'.format(gst(10000,500)))
	print('{:1.4}'.format(gst(20000,200)))
	print('{:1.4}'.format(gst(30000,100)))