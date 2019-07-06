'''
% [kepel] = statvec_kepel (statv)
%
%	The function statvec_kepel transforms the state vector statv
%	into the corresponding keplerian elements in the
%	same reference system.
%
% Input:
%	statv
%		state vector in meters and meters/second.
%
% Output:
%	statvec_kepel
%		vector containing the keplerian elements:
%		(1) - semimajor axis of the orbit in meters.
%		(2) - eccentricity.
%		(3) - inclination in radians.
%		(4) - right ascension of ascending node in radians.
%		(5) - argument of perigee in radians.
%		(6) - mean anomaly in radians.
%
% Authors:
%	Helio K. Kuga
%   Valder M. Medeiros
%	Valdemir Carrara			february/80			version 1.0
%	Helio K. Kuga     			august/82           version 2.0
%	Ulisses T V Guedes 			december/95	 		version 2.1
%               - fix perigee procedure when orbit plane
%                  equal to equatorial plane
%	Valdemir Carrara 			july/05				(C version)
%   Valdemir Carrara            March/09   

'''

import math
import numpy as np

def statvec_kepel(statv):

	np.set_printoptions(precision=4) #print options to numpy

	EARTH_GRAVITY = 3.9860064e+14 #Earth's gravitational constant (m^3/s^2)

	kepel = np.zeros(5)
	xp    = statv[0:3]
	xv    = statv[3:]
	r     = math.sqrt(np.dot(xp, xp.T))
	vq    = np.dot(xv, xv.T)
	ainv  = 2.0/r - vq/EARTH_GRAVITY
	h     = np.cross(xp, xv)
	hm    = math.sqrt(np.dot(h, h.T))

	#print('r : {:.4}'.format(r))
	#print('vq : {:.4}'.format(vq))
	#print('ainv : {:.4}'.format(ainv))
	#print('h : {0}'.format(h))
	#print('hm : {:.4}'.format(hm))

	if hm < (1.0e-10):

		print('*** Message from function statvec_kepel: ***')
		print('There are no keplerian elements corresponding to this state vector')
		return kepel

	else:
		
		h     = h/hm
		incl  = math.acos(h[2])
		raan  = math.atan2(h[0], -h[1])
		d     = np.dot(xp, xv.T) / EARTH_GRAVITY
		esene = d * math.sqrt(EARTH_GRAVITY*ainv)
		ecose = 1 - r*ainv
		exc   = math.sqrt(esene**2 + ecose**2)
		E     = math.atan2(esene, ecose)
		mean  = (E - esene) % (2*math.pi)

		#print('h : {0}'.format(h))
		#print('incl : {:.4}'.format(incl))
		#print('raan : {:.4}'.format(raan))
		#print('d : {:.4E}'.format(d))
		#print('esene : {:.4E}'.format(esene))
		#print('ecose : {:.4}'.format(ecose))
		#print('exc : {:.4}'.format(exc))
		#print('E : {:.4}'.format(E))
		#print('mean : {:.4}'.format(mean))
		#print('------------------------------')

		if mean < 0:
			mean = mean + 2*math.pi

		if exc < (1.0e-10):
			arpe = 0
		else:
			dp    = 1.0/r - ainv #escalar
			ev    = dp*xp - d*xv #vetor
			abev  = math.sqrt(np.dot(ev, ev.T)) #escalar
			ev    = ev/abev #vetor
			an    = np.array([ math.cos(raan),
							   math.sin(raan),
								   0       ])
			fi    = np.dot(ev, np.cross(h, an).T)
			arpe  = math.acos(np.dot(ev, an.T))

			#print('dp : {:.4}'.format(dp))
			#print('ev : {0}'.format(ev))
			#print('abev : {:.4}'.format(abev))
			#print('ev : ',ev)
			#print('fi : ',fi)
			#print('arpe : ',arpe)

			if fi < 0:
				arpe = 2*math.pi - arpe
				#print('arpe : ',arpe)

	kepel = np.array([1.0/ainv,  exc, incl,
						  raan, arpe, mean])

	return kepel

if __name__ == "__main__":
	r = np.array([0.1, 0.01, 0.01, 0.1, 0.1, 0.1])
	p = np.array([0.01, 0.02, 0.02 ,0.2 ,0.01 ,0.01])
	q = np.array([0.05, 0.01, 0.03, 0.01, 0.05,0.07])
	s = np.array([1, 1, 1, 1, 1, 1])
	print('Args : {0}'.format(q))
	print('Kepel : {0}'.format(statvec_kepel(q)))