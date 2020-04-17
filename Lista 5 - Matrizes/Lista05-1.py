#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 1

#linhaXcoluna
#l eh linha
#c eh coluna

m = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+": ")) for c in range(6)] for l in range(3)]

print "\n",m,"\n"
print max(m),"\n"
print min(m),"\n"
print "O maior elemento:", max(max(m))
print "O menor elemento:", min(min(m))
