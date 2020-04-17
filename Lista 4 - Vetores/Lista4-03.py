#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 3

vetor = []

for i in xrange(1,21):
    if i%2 != 0:
        impar = i*i
        vetor.append(impar)

for i in xrange(len(vetor)):
    print vetor[i]
