#Author: Lucas Pereira Torres de Araujo
#Lista 5 - FUP's Class - 2016.1
#Item 9

#linhaXcoluna
#l eh linha
#c eh coluna

#mA = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz A: ")) for c in range(2)] for l in range(3)]
#mB = [[int(input("Digite um elemento para posicao "+str(l+1)+"x"+str(c+1)+" da matriz B: ")) for c in range(5)] for l in range(2)]

mA = [[1,2],[3,4],[5,6]]
mB = [[1,2,3,4,5],[6,7,8,9,10]]
mC = []

print "Matriz A:"
for j in mA:
	print j

print "\nMatriz B:"
for j in mB:
	print j

for i in xrange(len(mA)):
	x = (mA[][]*mB[][] + mA[][]*mB[][]) for k in xrange(len(len(mB))
	mC.insert(i, x)

print

3x2
[1 (00), 2 (01)]
[3 (10), 4 (11)]
[5 (20), 6 (21)]
2x5
[1 (00), 2 (01), 3 (02), 4 (03), 5  (04)]
[6 (10), 7 (11), 8 (12), 9 (13), 10 (14)]

3x5
(1*1 + 2*6)   (1*2 + 2*7)   (1*3 + 2*8)   (1*4 + 2*9)   (1*5 + 2*10)
(3*1 + 4*6)   (3*2 + 4*7)   (3*3 + 4*8)   (3*4 + 4*9)   (3*5 + 4*10)
(5*1 + 6*6)   (5*2 + 6*7)   (5*3 + 6*8)   (5*4 + 6*9)   (5*5 + 6*10)

(mA[0][0]*mB[0][0] + mA[0][1]*mB[1][0])   (mA[0][0]*mB[0][1] + mA[0][1]*mB[1][1])   (mA[0][0]*mB[0][2] + mA[0][1]*mB[1][2])   (mA[0][0]*mB[0][3] + mA[0][1]*mB[1][3])   (mA[0][0]*mB[0][4] + mA[0][1]*mB[1][4])

(mA[1][0]*mB[0][0] + mA[1][1]*mB[1][0])   (mA[1][0]*mB[0][1] + mA[1][1]*mB[1][1])   (mA[1][0]*mB[0][2] + mA[1][1]*mB[1][2])   (mA[1][0]*mB[0][3] + mA[1][1]*mB[1][3])   (mA[1][0]*mB[0][4] + mA[1][1]*mB[1][4])

(mA[2][0]*mB[0][0] + mA[2][1]*mB[1][0])   (mA[2][0]*mB[0][1] + mA[2][1]*mB[1][1])   (mA[2][0]*mB[0][2] + mA[2][1]*mB[1][2])   (mA[2][0]*mB[0][3] + mA[2][1]*mB[1][3])   (mA[2][0]*mB[0][4] + mA[2][1]*mB[1][4])