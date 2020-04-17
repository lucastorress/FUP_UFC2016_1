#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 10

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(3)] for l in range(3)]
#m = [[1,2,3],[4,5,6],[7,8,9]]
diagonalp = []
diagonals = []

print "Matriz:"
for j in m:
	print j

for n in xrange(len(m)):
	for k in xrange(len(m)-1):
		m[n].append(m[n][k])

print "\nRegra de Sarrus:"
for j in m:
	print j

for x in xrange(3):
	diagonalp.append(m[x][x])

for x in xrange(3):
	diagonalp.append(m[x][x+1])

for x in xrange(1,4):
	diagonalp.append(m[x-1][x+1])

detp = (diagonalp[0]*diagonalp[1]*diagonalp[2])+(diagonalp[3]*diagonalp[4]*diagonalp[5])+(diagonalp[6]*diagonalp[7]*diagonalp[8])

for x in xrange(3):
	diagonals.append(m[2-x][x])

for x in xrange(3):
	diagonals.append(m[2-x][x+1])

for x in xrange(3):
	diagonals.append(m[2-x][x+2])

dets = (diagonals[0]*diagonals[1]*diagonals[2])+(diagonals[3]*diagonals[4]*diagonals[5])+(diagonals[6]*diagonals[7]*diagonals[8])

det = detp - dets

#print diagonalp
#print diagonals
print "\nValor da determinante:",det
