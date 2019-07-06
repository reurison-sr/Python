"""
The function djm_inv gives the date corresponding to
a given mjd (Modified Julian Date) date

Input:
   mjd = Modified Julian Date in days, referred to 1950.0.

Output:
   date = [day, month, year]

Matlab Version: Valdemir Carrara, Feb, 2009
Python Version: Reurison Silva, Abr, 2019
"""

import numpy as np

def djm_inv(mjd):

	DEBUG = 0

	d1 = np.array([0, 31, 61, 92, 122, 153, 184,
	              214, 245, 275, 306, 337, 366])

	y4   = 0
	y1   = 0
	d    = int(mjd + 127775)
	y400 = int(d/146097)
	d    = d - y400*146097
	y100 = int(d/36524)
	d    = d - y100*36524

	if DEBUG:
		print('mjd : {0}'.format(mjd))
		print('y4 : {0}'.format(y4))
		print('y1 : {0}'.format(y1))
		print('y400 : {0}'.format(y400))
		print('y100 : {0}'.format(y100))
		print('d : {0}'.format(d))

	if y100 > 3:

		dat1 = 29
		dat2 = 2
		dat3 = 1600 + y400*400 + y100*100 + y4*4 + y1

	else:

		y4   = int(d/1461)
		d    = d - y4*1461
		y1   = int(d/365)

		if y1 > 3:

			dat1 = 29
			dat2 = 2
			dat3 = 1600 + y400*400 + y100*100 + y4*4 + y1

		else:

			d    = d - y1*365
			i    = int(d/32 + 2)
			d    = d + 1


	if DEBUG:
		print('----------------------')
		print('y4 : {0}'.format(y4))
		print('y1 : {0}'.format(y1))
		print('d  : {0}'.format(d)) #37
		print('i  : {0}'.format(i))
		print('----------------------')
	
	#Atenção ao índice do d1. Daqui para baixo pode dar um erro.

	while d1[i-1] < d:
		i += 1

	dat2 = i + 1 #OK
	dat1 = d - d1[i-2] 
	dat3 = 1600 + y400*400 + y100*100 + y4*4 + y1 #OK

	if DEBUG:
		print('dat1 : {0}'.format(dat1))
		print('dat2 : {0}'.format(dat2))
		print('dat3 : {0}'.format(dat3))

	if dat2 > 12:
		dat2 = dat2 - 12
		dat3 = dat3 + 1

	date = np.array([dat1, dat2, dat3])
	return date

if __name__ == "__main__":
	#djm_inv(18000)
	print('0: {0}'.format(djm_inv(0)))
	print('1: {0}'.format(djm_inv(1)))
	print('5: {0}'.format(djm_inv(5)))
	print('10: {0}'.format(djm_inv(10)))
	print('11111: {0}'.format(djm_inv(11111)))
	print('22222: {0}'.format(djm_inv(22222)))
	print('44444: {0}'.format(djm_inv(44444)))
	print('55555: {0}'.format(djm_inv(55555)))
	print('66666: {0}'.format(djm_inv(66666)))
	print('77777: {0}'.format(djm_inv(77777)))
	print('88888: {0}'.format(djm_inv(88888)))
	print('99999: {0}'.format(djm_inv(99999)))
