#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 7

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(4)] for l in range(4)]
#m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

diagonals = []

print "Antiga matriz:"
for j in m:
	print j

for x in xrange(4):
	diagonals.append(m[x][3-x])

#print "\n",diagonals,"\n"

for i in xrange(len(m)):
	if m[i][3-i] == diagonals[i]:
		del m[i][3-i]

print "Nova matriz:"
for j in m:
	print j
