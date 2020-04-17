#Lista 4 - FUP's Class - 2016.1
#Item 20

soma = 0
menor = 0
maior = 0
aux = 0

v = []
n = input("Digite quantos numeros deseja na lista: ")

for i in xrange(n):
    n1 = input("Digite o numero de indice "+str(i)+"o: ")
    v.append(n1)

for i in xrange(n):
    for j in xrange(n):
        aux += v[j]
        if aux > soma:
            maior = j
            menor = i
            soma = aux
    aux = 0

print "Maior soma encontrada:", soma
print v[menor]
print v[maior]
