#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 8

vequal = []
vrepeat = []

n = input("Digite o valor de n: ")

for j in xrange(n):
	x = input("Digite os numeros em ordem crescente: ")
	vequal.insert(j, x)
	
anterior = vequal[0]
vezes = 1
vrepeat.append(vequal[0])
j = 1

for i in xrange(1, n):
	if (vequal[i] == anterior):
		vezes += 1
	else:
		print "O numero ",anterior," se repete ",vezes," vezes."
		j += 1
		vrepeat.append(vequal[i])
		anterior = vequal[i]
		vezes = 1

print "O numero ",anterior," se repete ",vezes," vezes."
print "O vetor sem numeros repetidos eh:"

for k in xrange(j):
	print vrepeat[k]
