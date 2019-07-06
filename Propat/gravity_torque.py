'''
    % [gra_torq] = gravity_torque(r_sat, c_b_i, inert)
    %   Function to evaluate the gravity gradient torque from satellite
    %   attitude.
    % inputs:
    %   r_sat
    %       Satellite orbit position in inertial frame (m) (kepel_statvec)
    %   c_b_i
    %      Satellite attitude matrix, with respect to the inertial frame.
    %      v_body = c_b_i * v_inertial
    %   inert
    %      Inertia matrix in kg m^2, in satellite coordinates
    %
    % outputs:
    %   gra_torq 
    %      Gravity gradient torque (spacecraft reference coordinates)
    %      in Nm
    %

    % Valdemir Carrara, Dec 2016
'''

import numpy as np
from gg_torque import gg_torque

def gravity_torque(r_sat, c_b_i, inert):

	np.set_printoptions(precision=4)

	r_nor =  np.linalg.norm(r_sat)
	vert = c_b_i.dot((r_sat/r_nor).T)
	ggamp = 3*(3.9860064e14)/(r_nor**3)
	gra_torq = gg_torque(ggamp, inert, vert)
	return gra_torq

if __name__ == "__main__":
	inert = np.array([ [0.0015,0,0], [0,0.0035,0], [0,0,0.004] ])
	r_sat = np.array([ 1500,2000,3500 ])
	c_b_i = np.array([ [0.5,0.2,0.5], [0.8,0,0.7], [0.1,0.12,0.15]])
	print(gravity_torque(r_sat, c_b_i, inert))