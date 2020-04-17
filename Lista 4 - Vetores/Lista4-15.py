#Lista 4 - FUP's Class - 2016.1
#Item 15

vetInt = []
media = 0
variancia = 0
#desviop = 0

n = int(input("Digite a quantidade N de numeros inteiros: "))

for i in xrange(n):
    x = float(input("Digite os valores: "))
    vetInt.append(x)

media = float(sum(vetInt)/n)

for i in xrange(n):
    desvio = float((vetInt[i] - media)**2)
    variancia += desvio

variancia = float(variancia/(n-1))
desviop = float(variancia**(0.5))

print "Media: ",media
print "Variancia: ",variancia
print "Desvio Padrao: ",desviop
