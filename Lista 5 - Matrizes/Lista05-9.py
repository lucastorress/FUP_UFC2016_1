#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 9

#linhaXcoluna
#l eh linha
#c eh coluna

mA = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(2)] for l in range(3)]
print "--- Fim da Matriz A ---"
mB = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz B: ")) for c in range(5)] for l in range(2)]
print "--- Fim da Matriz B ---"
mC = [[int(0) for k in xrange(5)] for n in xrange(3)]

#mA = [[1,2],[3,4],[5,6]]
#mB = [[1,2,3,4,5],[6,7,8,9,10]]
#mC = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print "\nMatriz A:"
for j in mA:
	print j

print "\nMatriz B:"
for j in mB:
	print j

for a in xrange(3):
	for b in xrange(5):
		mC[a][b] = mA[a][0]*mB[0][b] + mA[a][1]*mB[1][b]

print "\nMatriz C:"
for j in mC:
	print j
