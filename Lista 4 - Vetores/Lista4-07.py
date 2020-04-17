#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 7

vetor = []
maiortemp = 0
menortemp = 0
dias = 0
media = 0
soma = 0

for j in xrange(5):
	x = float(input("Digite a temperatura em Celsius: "))
	vetor.insert(j, x)
	
	if (vetor[j] < menortemp) or (j == 1):
		menortemp = vetor[j]
	
	if (vetor[j] > maiortemp) or (j == 1):
		maiortemp = vetor[j]
		
	soma = soma + vetor[j]

media = soma/5.0

for i in xrange(5):
	if (vetor[i] < media):
		dias = dias + 1

print "A menor temperatura ocorrida eh: ", menortemp
print "A maior temperatura ocorrida eh: ", maiortemp
print "A temperatura media eh: ", media
print "Numero de dias nos quais a temperatura foi inferior a media: ", dias
