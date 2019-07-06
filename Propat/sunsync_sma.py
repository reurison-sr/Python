'''
%   This function obtains the orbital semimajor axis of a low Earth orbit
%   given the orbital recovering factor q.
%  
%   Inputs:
%       exc
%           Orbital excentricity
%       inc
%           Orbital inclination (rad)
%       q 
%           Sun-synchronous orbit recovering factor. The recovering factor 
%           is calculated by q = N + M / I, where N, M and I are integers. 
%           N is the number of orbits per day, M is the exceeding orbits 
%           after I days, and I is the recovering period in days. The 
%           recovering factor normally lies between 13 to 16.
%
%   Output:
%       smaxis
%           Recurrent orbital semimajor axis, in meters.
%
%   Author:
%       Valdemir Carrara        Feb. 1992      V 1.0
%       Valder Matos de Medeiros    Mai. 1997
%       Valdemir Carrara        May/2017        Matlab version
% 

'''

import math
import numpy as np
from delkep import delkep

def sunsync_sma(exc, inc, q):

	np.set_printoptions(precision=4)

	EARTH_GRAVITY = 3.9860064e+14 # Earth's gravity (m^33/s^2)
	EARTH_RATE    = 7.2921158546819492e-5 # Earth's sidereal rotation speed (rad/s) = (1+1/TROPIC_YEAR)*PI_T2/86400

	el   = np.array([6878000, exc, inc, 0, 0, 0])
	ant  = el[0]
	epx  = -1.5*math.sqrt(EARTH_GRAVITY/(ant**5))
	del_ = 1000000
	ic   = 0

	while ( (abs(del_/ant) > 1.0e-9) and (ic < 20)):

		delk  = delkep(el) #funcao delkep
		#print('delk : ', delk)
		fact  = delk[4] + delk[5] - q*(EARTH_RATE - delk[3])
		#print('fact : {:.4}'.format(fact))
		del_  = fact/epx
		#print('del_ : {:.4}'.format(del_))
		sma   = ant - del_
		#print('sma : {:.4}'.format(sma))
		ant   = sma
		#print('ant : {:.4}'.format(ant))
		el[0] = sma
		#print('el[0] : {:.4}'.format(el[0]))
		ic    = ic + 1
	
	if (ic > 30):
		print('''Error in routine sunsync_recf. 
			  Interaction did not converge''')
		return None
	else:
		smaxis = sma
		return smaxis

if __name__ == "__main__":

	#exc = 0.0167
	#inc = 0.5
	#q = 14
	exc = 0.03
	inc = 0.3555
	q = 15
	sunsync_sma(exc, inc, q)

