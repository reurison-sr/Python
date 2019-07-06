'''
% equação da visviva
% entradas:
%    a    Semi-eixo maior da órbita (m).
%    r    Altitude do satélite num dado instante (m)
% saídas:
%    vi   Velocidade do satélite no ponto dado por r.
% Valdemir Carrara (11/2014)

'''

import math

def visviva(a, r):

	mu = 3.986e14
	vi = math.sqrt(mu*(2/r - 1/a))
	return vi

if __name__ == "__main__":
	print(visviva(10000, 10000))