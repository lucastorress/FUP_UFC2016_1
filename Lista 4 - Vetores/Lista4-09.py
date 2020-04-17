#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 9

vetor = []
soma = 0

for j in xrange(100):
    x = input("Digite o " + str(j) + "o valor numerico: ")
    vetor.insert(j,x)

for j in xrange(50):
    soma += (vetor[j] - vetor[101-j]) * (vetor[j] - vetor[101-j]) * (vetor[j] - vetor[101-j])

print "O valor do somatorio eh:", soma
