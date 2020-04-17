#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 13

#linhaXcoluna
#l eh linha
#c eh coluna

flag = 1

while flag == 1:
	n = input("Digite o valor de N para matriz NxN com N < 10: ")
	if n < 10:
		flag = 0

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(n)] for l in range(n)]

sit = 1

for i in xrange(n):
	for j in xrange(i, n):
		if m[i][j] != m[j][i]:
			sit = 0

if sit == 1:
	print "A matriz eh simetrica."
else:
	print "A matriz nao eh simetrica."
