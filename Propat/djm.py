""""
    The function djm furnishes the Modified Julian
    Date with reference to the day, month and year,
    at zero hours of the day.

Input
   day   = day of the month.
   month = month of the year.
   year  = year.

Output: 
	diju = Modified Julian Date in days, referred to 1950.0. 

Matlab Version: Valdemir Carrara, Apr, 2003
Python Version: Reurison Silva, Apr, 2019.
"""

def djm(day, month, year):

	diju = (367*year) + (day - 712269) + int( 275*month/9 ) \
	       - int(7*( year + int( ( month+9 ) / 12 ) ) / 4 )

	return diju

if __name__ == "__main__":
	print(djm(11, 9, 1900))
	print(djm(3, 1, 1991))
	print(djm(3, 8, 1992))
	print(djm(22, 4, 1962))
	print(djm(11, 9, 2001))
	print(djm(12, 9, 2001))