#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 10

faturamento = 0
preco = []

for j in xrange(5):
	x = input("Digite o preco de venda da mercadoria n." + str(j) +": ")
	preco.insert(j, x)

for j in xrange(5):
	n = input("Digite a quantidade vendida da mercadoria n." + str(j) +": ")
	faturamento += n*(preco[j])

print "O faturamento eh: ", faturamento
