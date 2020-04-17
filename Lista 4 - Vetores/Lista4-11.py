#Lista 4 - FUP's Class - 2016.1
#Item 11

vetorx = []
vetorc = []
n = input("Digite o valor de n: ")

for j in xrange(n):
    x = input("Digite o coeficiente a"+str(j)+": ")
    vetorc.insert(j,x)

for j in xrange(10):
    x = input("Digite o "+str(j)+" valor de x: ")
    vetorx.insert(j,x)

for j in xrange(10):
    p = vetorc[0]
    for i in xrange(n):
        expoente = 1
        for k in xrange(i):
            expoente = expoente * vetorx[j]
        p = p + vetorc[i]*expoente
    print "A soma P de x"+str(j)+" eh: ",p
