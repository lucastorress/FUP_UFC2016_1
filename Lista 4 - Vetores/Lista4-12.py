#Lista 4 - FUP's Class - 2016.1
#Item 12

vetor = []
n = input("Digite o valor de N: ")

for j in xrange(n):
    x = input("Digite os valores numericos da variavel composta: ")
    vetor.insert(j,x)

k = input("Digite o valor de K: ")
print "O k-esimo termo antes da ordenacao eh: ",vetor[k]

for j in xrange(n-1):
    for i in xrange(n-j):
        if vetor[i] > vetor[i+1]:
            aux = vetor[i]
            vetor[i] = vetor[i+1]
            vetor[i+1] = aux

print "O k-esimo termo depois da ordenacao eh: ",vetor[k]
