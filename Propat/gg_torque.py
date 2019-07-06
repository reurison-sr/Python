'''
% [gra_torq] = gg_torque (ggamp, inert, vertic)
%   Function to evaluate the gravity gradient torque
% inputs:
%   ggamp     
%      3*Gm/(R^3), where Gm is the Earth's gravitational constant
%      (Gm = 3.9860064 E+14 m^3/s^2) and R is the geocentric 
%      distance in meters
%   inert
%      Inertia matrix in kgm^2, in satellite coordinates
%   vertic
%      Local vertical unit vector (towards zenith) in satellite
%      coordinates
%
% outputs:
%   gra_torq 
%      Gravity gradient torque (spacecraft reference coordinates)
%      in Nm
%

% Valdemir Carrara, Sep 1999
'''

import numpy as np

def gg_torque(ggamp, inert, vertic):

	#np.set_printoptions(precision=4)
	gra_torq = ggamp*np.cross(vertic, inert.dot(vertic))
	return gra_torq


if __name__ == "__main__":

	#GM = 3.9860064E+14
	#R = 3500
	#ggamp = 3*GM/(R**3)
	#inert = np.array([ [0.15,0,0], [0,0.35,0], [0,0,0.4] ])
	#vertic = np.array([1, 1, 1])
	ggamp = 2.2828e+13
	inert = np.array([ [0.015,0,0], [0,0.035,0], [0,0,0.04] ])
	vertic = np.array([ 0.6414, 0.7751, 0.2111 ])

	print(gg_torque(ggamp, inert, vertic))