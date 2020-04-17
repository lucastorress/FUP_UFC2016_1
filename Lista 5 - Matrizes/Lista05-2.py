#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 2

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(4)] for l in range(4)]

diagonalp = []

for x in xrange(4):
	diagonalp.append(m[x][x])
	#print "Posicao "+str(x)+"x"+str(x)+":",m[x][x]

print diagonalp