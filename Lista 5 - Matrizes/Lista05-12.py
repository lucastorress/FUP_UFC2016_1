#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 12

#linhaXcoluna
#l eh linha
#c eh coluna

flag = 1

while flag == 1:
	n = input("Digite o valor de N para matriz NxN com N < 10: ")
	if n < 10:
		flag = 0

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(n)] for l in range(n)]
#m = [[1,2,3],[4,5,6],[7,8,9]]
#m = [[1,2],[3,4]]
c = m

print "Matriz:"
for j in m:
	print j

for a in xrange(len(m)):
	for b in xrange(len(m)):
		c[b][a] = m[a][b]

print "Matriz:"
for j in c:
	print j
