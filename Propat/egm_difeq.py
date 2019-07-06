'''
% dxdt = egm_difeq (time, x, flag, ext_forces)
%
%   The egm_difeq function returns with the time derivative of the 
%   satellite orbit position and velocity. The gravity model is internally 
%   computed by the egm functions. However, the egm model has to be
%   initialized by calling the egm_read_dat function. See the egm_read_data
%   function for description.
%
% inputs:
%   time
%       Propagation time (s)
%   x
%       Orbit state vector: position (m) (1:3) and velocity (m/s) (4:6)
%   flag
%       See ODEFILE
%   mjd
%       Modified Julian date referred to 1950.
%   dsec
%       Day time UTC in seconds of initial orbit ephemeris. Current time
%       is (dsec + time)
%   ext_acc
%       External specific forces (acceleration) acting on the spacecraft 
%       (m/s2) including control (thrusters, orbit correction and 
%       disturbances), except gravity.
% outputs:
%   dxdt 
%       Time derivative (velocity and acceleration) of the state vector
% 
% author:
%   Valdemir Carrara,   July, 2017.

'''

import numpy as np

from gst import gst
from inertial_to_terrestrial import inertial_to_terrestrial 
from terrestrial_to_inertial import terrestrial_to_inertial
#from egm_acc import egm_acc #implementar

def egm_difeq(time, x, flag, mjd, dsec, ext_acc):

	np.set_printoptions(precision=4)

	xip  = x[3:6]
	gwst = gst(mjd, dsec + time) #funcao gst
	se   = inertial_to_terrestrial(gwst, x)
	xe   = se[0:3]

	#print("xip : {0}".format(xip))
	#print("gwst : {0}".format(gwst))
	#print("se : {0}".format(se))
	#print("xe : {0}".format(xe)) 

	#ae   = [egm_acc(xe); 0; 0; 0]
	#Forçando o valor de ae
	ae = np.array([1,2,3,0,0,0])
	ai   = terrestrial_to_inertial(gwst, ae)
	vip  = ext_acc + ai[0:3]

	#print('ae : {0}'.format(ae))
	#print('ai : {0}'.format(ai))
	#print('vip : {0}'.format(vip))

	dxdt = np.hstack((xip, vip))
	#print('dxdt : {0}'.format(dxdt))

	return dxdt

if __name__ == "__main__":
	time = 3600
	flag = 0
	x = np.array([1,2,3,4,5,6])
	mjd = 30000
	dsec = 7200
	ext_acc = np.array([1,2,3])
	print(egm_difeq(time, x, flag, mjd, dsec, ext_acc))