#Lista 4 - FUP's Class - 2016.1
#Item 17

produto = 0
vetorX = []
vetorY = []

tamanho = int(input("Digite o tamanho dos vetores: "))

for i in xrange(tamanho):
    x = input("Digite os componentes do vetor x: ")
    vetorX.insert(i, x)
    
for i in xrange(tamanho):
    y = input("Digite os componentes do vetor y: ")
    vetorY.insert(i, y)

for i in xrange(tamanho):
    produto += (vetorX[i] * vetorY[i])

print "O produto escalar desses vetores eh:",produto
