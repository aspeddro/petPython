# Questão 1
from math import sqrt

def raiz(a,b,c):
	delta = (b**2)-4*a*c
	if delta < 0:
		return 'Não existe solução'
	x1 = (-b+sqrt(delta))/(2*a)
	x2 = (-b-sqrt(delta))/(2*a)
	return (x1, x2)

#print(raiz(2,-6,-12))

# Questão 2

def dist(x1, x2, y1, y2):
	xd = (x2 - x1)**2
	yd = (y2 - y1)**2
	distancia = sqrt(xd + yd)
	return distancia

# print(dist(4, 2, 5, -3))

# Questão 3

def gasto(distancia, consumo, valor):
	"""O programa deve ter em seu algoritmo o valor da distância a ser percorrida em Km, o consumo do carro em Km por litros e o valor em reais do litro do combustível da viagem."""
	"""calcule o gasto com combustível em uma viagem??"""
	gasto = distancia*valor
	gasto_total = gasto / consumo
	return gasto_total


# print(gasto(distancia=10, consumo=2, valor=4.5))


# Questão 4
def rachadinha(total):
	"""Três amigos, Carlos, André e Felipe decidiram rachar igualmente a conta de um bar. Faça um algoritmo que tendo o valor total da conta, imprima quanto cada um deve pagar. Mas, faça com que Carlos e André não paguem centavos. Ex.: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para Felipe"""
	## 33.84
	resto = total % 3
	carlos = total // 3
	andre = total // 3
	felipe = (total // 3) + resto

	return {
		"Carlos": carlos,
		"Andre": andre,
		"Felipe": felipe
	}

# print(rachadinha(total=230.27))