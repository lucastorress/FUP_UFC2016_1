#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 14

#linhaXcoluna
#l eh linha
#c eh coluna

flag = 1

while flag == 1:
	n = input("Digite o valor de N para matriz NxN com N < 10: ")
	if n < 10:
		flag = 0

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(n)] for l in range(n)]
mt = [[int(0) for c in xrange(n)] for l in xrange(n)]
ms = [[int(0) for c in xrange(n)] for l in xrange(n)]

for i in xrange(n):
	for j in xrange(n):
		mt[i][j] = m[j][i]
		ms[i][j] = -m[i][j]

sit = 1
for i in xrange(n):
	for j in xrange(n):
		if mt[i][j] != ms[i][j]:
			sit = 0

if sit == 1:
	print "A matriz A eh anti-simetrica."
else:
	print "A matriz A nao eh anti-simetrica."
