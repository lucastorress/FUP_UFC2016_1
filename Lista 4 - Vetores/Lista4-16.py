#Lista 4 - FUP's Class - 2016.1
#Item 16

gabarito = []
respostas = []

n = input("Digite o numero de alunos: ")

for i in xrange(5):
    x = raw_input("Digite o gabarito da prova: ")
    gabarito.append(x)

for aluno in xrange(1, n+1):
    pontos = 0
    for i in xrange(5):
        x = raw_input("Digite as respostas do aluno "+str(aluno)+": ")
        respostas.insert(i,x)
        if respostas[i] == gabarito[i]:
            pontos += 1
    print "O aluno "+str(aluno)+" acertou "+str(pontos)+" questoes."
