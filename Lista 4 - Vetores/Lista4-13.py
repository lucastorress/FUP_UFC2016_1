#Lista 4 - FUP's Class - 2016.1
#Item 13

vetNome = []
vetVoto = []
voto = "inicio"
flag = 0

#Receber quantidade de chapas
n = int(input("Digite o numero de chapas a concorrer as eleicoes: "))

#Receber os nomes das chapas
for j in xrange(1, n+1):
    x = raw_input("Digite o "+str(j)+"o. ")
    vetNome.append(x)
    vetVoto.append(0)

#Receber os votos e checar o fim
while voto != "fim":
    voto = raw_input("Digite o nome do candidato: ")

    for k in xrange(n):
        if voto == vetNome[k]:
            vetVoto[k] += 1

vencedor = max(vetVoto)

for i in xrange(n):
    if vetVoto[i] == vencedor:
        print "Vencedor:",vetNome[i]
        flag += 1

if flag >= 2:
    print "Resultado final: Empate."
