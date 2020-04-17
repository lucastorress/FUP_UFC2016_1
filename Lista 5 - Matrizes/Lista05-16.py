#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 16

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(3)] for l in range(3)]
mf = [[int(0) for k in xrange(len(m))] for n in xrange(len(m))]

for i in xrange(len(m)):
	for j in xrange(len(m)):
		mf[j][len(m)-i-1] = m[i][j]

print "\nMatriz:"
for j in m:
	print j

print "\nMatriz 90 graus:"
for j in mf:
	print j
