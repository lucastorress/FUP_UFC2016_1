#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 11

#linhaXcoluna
#l eh linha
#c eh coluna

#n = input("Digite o valor de N para matriz NxN com N < 10: ")

#m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(n)] for l in range(n)]
m = [[1,2,3],[4,5,6],[7,8,9]]
#m = [[1,2],[3,4]]
c = m

print "Matriz:"
for j in m:
	print j

for a in xrange(3):
	for b in xrange(3):
		c[b][a] = m[a][b]

print "Matriz:"
for j in c:
	print j


[1 (00), 2 (01)]
[3 (10), 4 (11)]

[1 (00), 3 (10)]
[2 (01), 4 (11)]

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

01 - 10
11 - 11
21 - 12

20 - 02
21 - 12
22 - 22

00 01 02
10 11 12
20 21 22

00 10 20
01 11 21
02 12 22
