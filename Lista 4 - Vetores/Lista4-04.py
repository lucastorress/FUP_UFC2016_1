#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 4

vetor = []
media = 0

for j in xrange(1,11):
    altura = input("Digite a altura do atleta " + str(j) + ": ")
    vetor.append(altura)

    media = media + altura

for i in xrange(len(vetor)):
    if vetor[i] > (media/10):
        print "Altura do atleta", i+1,":",vetor[i]
