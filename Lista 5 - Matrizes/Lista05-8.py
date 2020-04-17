#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 8

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(5)] for l in range(3)]
#m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
soma = []

print "\nMatriz:"
for j in m:
	print j

for i in xrange(len(m)):
	soma.append(sum(m[i]))

print "\n",soma
