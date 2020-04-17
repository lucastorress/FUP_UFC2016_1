#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 3

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(4)] for l in range(4)]

diagonals = []
	
for x in xrange(4):
	diagonals.append(m[x][3-x])

print diagonals