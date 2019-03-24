#Validação de número de CPF.
#Algoritmo: http://www.macoratti.net/alg_cpf.htm


def validacao_cpf(cpf):

	"""Algoritmo que determina se o CPF é válido ou não"""

	if len(cpf) != 11:
		return False

	#Se cpf = 00000000000, 11111111111, ..., 99999999999.
	if cpf in [11*str(i) for i in range(0, 10)]:
		return False

	cpf = [int(i) for i in cpf]

	#Dígitos verificadores 1 e 2
	D1 = 0
	D2 = 0

	#Cálculo do primeiro digito verificador.
	multiplicador1 = [m for m in range(10, 1, -1)]
	resultado1 = [a*b for a,b in zip(cpf[:9], multiplicador1)]
	resto1 = sum(resultado1) % 11
	
	#Cálculo do segundo digito verificador.
	multiplicador2 = [m for m in range(11, 1, -1)]
	resultado2 = [a*b for a,b in zip(cpf[:10], multiplicador2)]
	resto2 = sum(resultado2) % 11

	if resto1 >= 2:
		D1 = 11 - resto1

	if resto2 >=2:
		D2 = 11 - resto2

	return (D1 == cpf[-2] and D2 == cpf[-1]) 


def det_estado(cpf):

	"""Função que determina de que estado o CPF é"""

	estados = {0:["RS"], 1:["DF, GO, MT, MS, TO"], 
			2:["PA, AM, AC, AP, RO, RR"],
			3:["CE, MA, PI"], 4:["PE, RN, PB, AL"], 5:["BA, SE"], 
			6:["MG"], 7:["RJ, ES"], 8:["SP"], 9:["PR, SC"]}

	return estados[int(cpf[-3])]


def main():

	lista = ["11111111111","22222222222", 
	         "55564646464664646", "00000",]

	for cpf in lista:
		if validacao_cpf(cpf):
			 print('CPF: {0} - Válido. Estado: {1}'.format(cpf, det_estado(cpf)))
		else:
			print('CPF: {0} - Inválido'.format(cpf))


if __name__ == "__main__":
	main()
