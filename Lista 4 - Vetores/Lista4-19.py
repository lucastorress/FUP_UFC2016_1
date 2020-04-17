#Lista 4 - FUP's Class - 2016.1
#Item 19

termos= []
sequencia = []
indices =[]

#Receber quantide de termos
n = int(input("Digite o numero de termos: "))

#Preencher vetor de termos
for i in range(0,n):
	num = int(input("Adicione um numero: "))
	termos.append(num)
	
print termos

for k in range(0,n):
	
	for l in range(k,n):
		if k!=l and termos[k]==termos[l]:
			sequencia.append(termos[k])
			indices.append(k)
			indices.append(l)			 

print "i:",indices[0]+1
print "m:",indices[1]-indices[0]
