#Crivo de Sundaram
#Source : https://en.wikipedia.org/wiki/Sieve_of_Sundaram

import isprime

def sundaram(N):

	"""
	Função que implementa o crivo de sundaram para
	encontrar os números primos no intervalo [1..N]
	"""

	primos = [i for i in range(1, N+1)]
	i = 1
	j_max = ((N - i))//(1 + 2*i)

	while (j_max > i):

		j = i
		
		while (j <= j_max):

			termo = i + j + 2*i*j
			if termo in primos:
				del primos[primos.index(termo)]
			j += 1

		i += 1
		j_max = ((N - i))//(1 + 2*i)

	return [(2*num + 1) for num in primos]



def main():

	N = int(input("Primos até : "))
	print(sundaram(N))
	#for num in sundaram(200):
	#	if not(isprime.e_primo(num)):
	#		print("ERROR")

if __name__ == "__main__":
	main()