'''
% function wns = rw_speed_n(x, rw_iner, an)
%   The function rw_speed_n gets the angular speed of the reaction wheels
%   given their angular momentum and rotation axis.
% inputs:
%   x
%       Attitude state vector: quaternions (4), angular velocity (rad/s) (3),
%       wheel's angular momentum (n)
%   rw_iner
%       Reaction wheel inertias around their rotation axis (kg*m*m).
%       Vector(n)
%   an
%       Matrix (3, n) with the n unit vectors of the reaction wheel
%       rotation axes.
% outputs:
%   wns      
%       Reaction wheel angular velocities. Vector(n).
%
% Valdemir Carrara, Sep, 2014.
'''

import numpy as np

#Esta função não está correta
# No argumento x(8:7+n), o valor de n é indefinido.
# Pode ser que seja alterado via usuário, neste caso OK
# Caso seja automático -> está faltando definir no programa


def rw_speed_n(x, rw_iner, an):


	wheel_ang_vel = x[4:7]
	print("wheel_ang_vel : {0}".format(wheel_ang_vel))

if __name__ == "__main__":

	x = np.array([1.1,1.5,1.8,0.5,10,10,10,3])
	rw_iner = np.array([1.15, 1.15, 1.15])
	an = np.array([ [1.1,1.2,1.3],
					[0.5,0.5,0.9],
					[0.7,0.8,1.7] ])
	rw_speed_n(x, rw_iner, an)