#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 5

vetor = []
ant1 = 0
ant2 = 1

for i in xrange(50):
    atual = ant1 + ant2
    vetor.append(atual)
    ant2 = ant1
    ant1 = atual

for j in xrange(len(vetor)):
    print vetor[j]
