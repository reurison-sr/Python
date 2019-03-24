#Implementação do crivo de erástotenes

def crivo(N):

	"""Função que implementa o crivo de erástotenes até um valor N"""

	crivo = [i for i in range(2, N)]

	for div in range(2, len(crivo)):

		for pos, num in enumerate(crivo):

			if div != num:
				if num % div == 0:
					del crivo[pos]
	return crivo

def main():

	N = int(input("Primos até : "))
	print(crivo(N))

if __name__ == "__main__":
	main()	
