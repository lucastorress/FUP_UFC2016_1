#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 19

#linhaXcoluna
#l eh linha
#c eh coluna

linha = 12
coluna = 4

m = [[input("Mes - "+str(l+1)+", Semana - "+str(c+1)+": ") for c in range(coluna)] for l in range(linha)]

tAno = 0

for i in xrange(linha):
	tMes = 0
	for j in xrange(coluna):
		tMes += m[i][j]
	
	print "Total do mes %d: %3.2f" % (i+1,tMes)
	tAno += tMes

for j in xrange(coluna):
	tSemana = 0
	for i in xrange(linha):
		tSemana += m[i][j]

	print "Total da semana %d: %3.2f" % (j+1,tSemana)

print "Total do ano: %3.2f" % tAno

print "\nMatriz:"
for j in m:
	print j
