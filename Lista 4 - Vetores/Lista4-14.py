#Nao concluido
#Lista 4 - FUP's Class - 2016.1
#Item 14

import copy

altura = []
sexo = []
nome = []

for i in xrange(3):
    x1 = raw_input("Digite a altura do individuo: ")
    x2 = raw_input("Digite o codigo do sexo (1-H/2-M): ")
    altura.append(x1)
    sexo.append(x2)

vetAltura = copy.deepcopy(altura)
#vetSexo = copy.deepcopy(sexo)

vetAltura.sort()

for i in xrange(3):
    x = raw_input("Digite o nome da pessoa, indice "+str(i)+":")

print altura
print sexo
print vetAltura
print nome
