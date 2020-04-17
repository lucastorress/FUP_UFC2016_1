#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 1

vetor = []

for i in xrange(100,201):
	vetor.append(i)

vetor.reverse() #Inverte a ordem dos valores da lista

for i in xrange(len(vetor)):
    print vetor[i]
