'''
[geodetic] = geocentric_to_sph_geodetic (geoc)
%	Function to transform rectangular terrestrial
%	geocentric coordinates in spherical geodetic
%	coordinates (longitude, latitude and altitude).
%
% Inputs:
%   geoc
%   		geocentric rectangular coordinates vector in meters
%           (1) geocentric position x (m)
%           (2) geocentric position y (m)
%           (3) geocentric position z (m)
%
% Outputs:
%	geodetic
%		Geodetic coordinates vector:
%			1 = east longitude (rad)
%			2 = geodetic latitude (rad)
%			3 = geodetic altitude (meters)
%
% Authors:
%	Helio K. Kuga				august/83		V. 1.0
%	Valdemir Carrara			08/05			C version
%   Valdemir Carrara            March/09        Matlab
'''

import math
import numpy as np

def geocentric_to_sph_geodetic(geoc):

	np.set_printoptions(precision=4)

	EARTH_FLATNESS = 0.0033528131778969144 #Flattening factor = 1./298.257
	EARTH_RADIUS    = 6378139.0 #Earth's radius in meters

	px = geoc[0]
	py = geoc[1]
	pz = geoc[2]
	gama = (1.0 - EARTH_FLATNESS) ** 2
	#gama = gama ** 2
	eps = 1.0 - gama
	as_ = EARTH_RADIUS**2
	ws  = px**2 + py**2
	zs  = pz**2
	zs1 = gama*zs
	e = 1.0

	# Maximum error in altitude dh
	det = 0.01*math.sqrt((2/3)/EARTH_RADIUS)
	de  = det*2

	#print("px : {0}".format(px))
	#print("py : {0}".format(py))
	#print("pz : {0}".format(pz))
	#print("gama : {0}".format(gama))
	#print("eps : {0}".format(eps))
	#print("as_ : {0:4E}".format(as_))
	#print("ws : {0}".format(ws))
	#print("zs : {0:4E}".format(zs))
	#print("zs1 : {0}".format(zs1))
	#print("det : {0:.5}".format(det))
	#print("de : {0:.5}".format(de))

	while (de > det):
		alf = e / (e - eps)
		zs2 = zs1*(alf**2)
		de  = 0.5*(ws + zs2 - as_*(e**2))/((ws + zs2*alf)/e)
		e = e + de

	#print('alf : {0:.5}'.format(alf))
	#print('zs2 : {0:.5}'.format(zs2))
	#print('de : {0:.5}'.format(de))
	#print(' e : {0}'.format(e))

	ss = (e - eps)
	ss = eps/(zs*zs*(ss**2))
	ro = EARTH_RADIUS*((1.0 + ss)/(2.0 + ss) + 0.25*(2.0 + ss))
	rw = e*ro

	#print('ss : {0:.5}'.format(ss))
	#print('ro : {0:.5}'.format(ro))
	#print('rw : {0:.5}'.format(rw))

	arl    = math.atan2(py, px)
	sf     = pz/(rw - eps*ro)
	cf     = math.sqrt(ws)/rw
	anorma = math.sqrt(sf**2 + cf**2)
	arf    = math.asin(sf/anorma)

	#print('arl : {0:.5}'.format(arl))
	#print('sf : {0:.5}'.format(sf))
	#print('cf : {0:.5}'.format(cf))
	#print('anorma : {0:.5}'.format(anorma))
	#print('arf : {0:.5}'.format(arf))

	geodetic = np.array([arl, arf, rw - ro])
	return geodetic

if __name__ == "__main__":
	A = np.array([200,250,35])
	print(geocentric_to_sph_geodetic(A))