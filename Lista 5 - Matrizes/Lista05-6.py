#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 6

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(4)] for l in range(4)]
#m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

diagonalp = []

print "Antiga matriz:"
for j in m:
	print j

for x in xrange(4):
	diagonalp.append(m[x][x])

#print diagonalp

for i in xrange(len(m)):
	if m[i][i] == diagonalp[i]:
		del m[i][i]

print "Nova matriz:"
for j in m:
	print j
