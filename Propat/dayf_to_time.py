"""
The function dayf_to_time computes the hour, minutes and seconds 
of the day based on the day elapsed time in seconds

Input: dayf = Day elapsed time in seconds. 

Output: day_time = [day_hour, minutes, seconds]
        hours = day hour (integer).
        minutes = minutes (integer).
        seconds = seconds and fraction of second

Matlab Version: Valdemir Carrara, Feb, 2009
Python Version: Reurisono Silva, Abr, 2019.
"""

import numpy as np

def dayf_to_time(dayf):

	#int : round towards zero.
	day1 = int(dayf/3600)
	day2 = int(dayf/60) - 60*day1
	day3 = dayf - 3600*day1 - 60*day2
	day_time = np.array([day1, day2, day3])
	return day_time

if __name__ == "__main__":
	print(dayf_to_time(3600))
	print(dayf_to_time(1))
	print(dayf_to_time(21))
	print(dayf_to_time(11))
	print(dayf_to_time(3))
	print(dayf_to_time(5))