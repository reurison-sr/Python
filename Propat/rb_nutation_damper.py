'''
% dxdt = rigbody (time, x, flag, ext_torque, tensin, teninv)
%   rigbody  returns with the time derivative of a rigid body
%   dynamic equations
% inputs:
%   time
%       Time (s)
%   x
%       Attitude state vector: quaternions (4), angular velocity (rad/s)
%       (3), nutation damper angular momentum (1) and nutation damper angle
%       (1).
%    
%   flag
%       See ODEFILE
%   ext_torque
%       External torques acting on the spacecraft (Nm) including control 
%       and unmodel disturbances.
%   tensin
%       Inertia matrix (kg*m*m).
%   teninv
%       Inverse of the inertia matrix (1/kg*m*m)
%   nd_axis
%       Direction of the nutation damper rotation axis, in spacecraft
%       frame (unit vector).
%   nd_inertia
%       Nutation damper moment of inertia (kg*m*m)
%   nd_spring
%       Nutation damper spring coefficient (Nm/rd)
%   nd_damper
%       Nutation damper coefficient (Nm s/rd)
% outputs:
%   dxdt       - State vector time derivative
% 

% Valdemir Carrara, Sep, 1998.
'''

import math
import numpy as np
from sangvel import sangvel


def rb_nutation_damper(time, x, flag, ext_torque, tensin,teninv,
					  nd_axis, nd_inertia, nd_spring, nd_damper):

	q = x[0:4]
	w = x[4:7]
	nd_momentum = x[7]
	nd_angle = x[8]

	nd_ang_vel = (nd_momentum - nd_inertia* np.dot(nd_axis.T,w))/nd_inertia;  # eq. 3.249
	xp = 0.5*np.dot(sangvel(w), q)
	torque = ext_torque

	nd_momentum_dot = -nd_spring*nd_angle - nd_damper*nd_ang_vel 
	nd_angle_dot = nd_ang_vel # eq. 3.253

	cross = np.cross(w, np.dot(tensin, w) + np.dot(nd_momentum, nd_axis)) #ok
	T1 = torque - cross - np.dot(nd_momentum_dot, nd_axis)
	wp = np.dot(teninv, T1) #ok

	stack_0 = np.hstack((nd_momentum_dot, nd_angle_dot))
	stack_1 = np.hstack((xp, wp))
	dxdt = np.hstack((stack_1, stack_0))
	
	return dxdt

if __name__ == "__main__":

	#Parâmetros obtidos de nutation_damper.m
	time = 0
	x = np.array([0,0,0,1,4,0,6,0.04,0])
	flag = 0
	ext_torque = np.array([0.5,0.9,1])
	tensin = np.diag([11.99,12,20])
	teninv = np.diag([0.0834,0.0833,0.0500])
	nd_axis = np.array([0,0,1])
	nd_inertia = 0.01
	nd_spring  = 0.16
	nd_damper  = 0.0020

	rb_nutation_damper(time, x, flag, ext_torque, tensin,
				teninv,nd_axis,nd_inertia,nd_spring,nd_damper)

