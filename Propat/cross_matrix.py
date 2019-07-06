"""To obtain the skew simetric matrix of the cross
product, ie: cross(w, v) = cross_matrix(w)*v

 Input: w vector (1,3)

 Output:

   cross_mat
       Cross product matrix (3x3), defined by:
         |    0,  -w(3),  w(2)|
         | w(3),      0, -w(1)|
         |-w(2),   w(1),     0|

   and 
       cross(w, v) = cross_matrix(w)*v
 
 Matlab version: Valdemir Carrara, Feb, 2008.
 Python version: Reurison Silva, Abr, 2019.
 """

import numpy as np

def cross_matrix(w):

	cross_mat = np.array([ [  0, -w[2],  w[1]],
 						           [+w[2],     0, -w[0]],
 						           [-w[1],  w[0],    0 ] ])
	return cross_mat

if __name__ == "__main__":
	print(cross_matrix(np.array([1,2,3])))
	print(cross_matrix(np.array([1,1,1])))
	print(cross_matrix(np.array([0,0,0])))
	print(cross_matrix(np.array([0.555,0.666,0.333])))
