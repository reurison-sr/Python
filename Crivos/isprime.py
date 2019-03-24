def e_primo(N):
	import math

	'''Funcao que determina se o número N é primo'''

	#Se o número for menor que 1 ou se for par diferente de dois.
	if N <= 1 or (N % 2 == 0 and N != 2):
		return False

	else:
		num_divisoes = 1 #Já considerando que é divisível por ele mesmo
		div = 1

		while div <= int(math.sqrt(N)):
			if N % div == 0:
				num_divisoes += 1
				if num_divisoes > 2:
					return False
			div += 1
		return True


def main():

	''' Testes para verificar funcao '''

	print('e_primo(10) : {0}'.format(e_primo(10) == False))
	print('e_primo(2)  : {0}'.format(e_primo(2)  == True ))
	print('e_primo(0)  : {0}'.format(e_primo(0)  == False))
	print('e_primo(-1) : {0}'.format(e_primo(-1) == False))
	print('e_primo(11) : {0}'.format(e_primo(11) == True ))
	print('e_primo(31) : {0}'.format(e_primo(31) == True ))
	print('e_primo(1)  : {0}'.format(e_primo(1)  == False))
	print('e_primo(20983) : {0}'.format(e_primo(20983) == True))
	print('e_primo(22549) : {0}'.format(e_primo(22549) == True))
	print('e_primo(22273) : {0}'.format(e_primo(22273) == True))
	print('e_primo(18353) : {0}'.format(e_primo(18353) == True))

if __name__ == "__main__":
	main()
