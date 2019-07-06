'''
% dxdt = rb_reaction_wheel (time, x, flag, ext_torque, tinerb, tinerbinv, rw_torque, rw_iner)
%   rb_reaction_wheel returns with the time derivative of the dinamic
%   equations of a rigid bod attached to 3 reaction wheels
% inputs:
%   time
%       Time (s)
%   x
%       Attitude state vector: quaternions (4), angular velocity (rad/s) (3),
%       wheel's angular momentum (3)
%   flag
%       See ODEFILE
%   ext_torque
%       External torques acting on the spacecraft (Nm) including control 
%       and unmodelled disturbances. Vector(3)
%   tinerb
%       Inertia matrix (kg*m*m) of the non-rotating mass, equal to the
%       difference between the total satellite inertia (including wheels) 
%       and the reaction wheel's rotating mass.
%       tinerb = inertia - rw_iner*identity(3,3). Matrix(3,3)
%   tinerbinv
%       Inverse of the tinerb inertia matrix (1/kg*m*m). Matrix(3,3)
%   rw_torque
%       Torque to be applied to the reaction wheels (Nm). Vector(3)
% outputs:
%   dxdt      
%       State vector time derivatives
% 

% Valdemir Carrara, Nov, 2013.

'''

import numpy as np
from sangvel import sangvel


def rb_reaction_wheel(time, x, flag, ext_torque, 
					tinerb, tinerbinv, rw_torque):

	q = x[0:4]
	w = x[4:7]
	hwn = x[7:]

	xp = 0.5*np.dot(sangvel(w), q)

	aux0 = np.dot(tinerb, w) + hwn
	aux1 = np.cross(aux0, w)
	aux2 = ext_torque + aux1 - rw_torque
	wp = np.dot(tinerbinv, aux2)
	hwnp = rw_torque
	dxdt = np.hstack((np.hstack((xp, wp)), hwnp))

	return dxdt

if __name__ == "__main__":

	#Parâmetros obtidos de nutation_damper.m
	time = 0
	x = np.array([0,0,0,1,4,0,6,0.04,0.5,0.6])
	flag = 0
	ext_torque = np.array([0.25,0.412,1.4554])
	tinerb     = np.diag([11.99,12,20])
	tinerbinv  = np.diag([0.0834,0.0833,0.0500])
	rw_torque    = np.array([0,0,0])
	print(rb_reaction_wheel(time, x, flag, ext_torque, 
					tinerb, tinerbinv, rw_torque))