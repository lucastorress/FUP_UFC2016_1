#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 2

vetor = []

for i in xrange(1,501):
    if i%5 == 0:
        vetor.append(i)

for i in xrange(len(vetor)):
    print vetor[i]
