#Nao concluido
#Lista 4 - FUP's Class - 2016.1
#Item 18

vetorX = []
vetorY = []
dist = 0

print "Digite as coordenadas do centro:"
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

n = int(input("Digite o numero de pontos: "))

while n <= 1 or n >= 100:
    n = int(input("Digite novamente: "))

for i in xrange(n):
    print "Digite as coordenadas dos pontos:"
    k1 = int(input("X1: "))
    j1 = int(input("Y1: "))
    k2 = int(input("X2: "))
    j2 = int(input("Y2: "))
