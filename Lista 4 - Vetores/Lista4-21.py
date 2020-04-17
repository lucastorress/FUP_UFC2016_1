#Lista 4 - FUP's Class - 2016.1
#Item 21

nAlunos = int(input("Digite a quantidade de alunos: "))
nProvas = int(input("Digite a quantidade de provas: "))
vetPeso = []
vetNota = []
vetAlNt = []
soma = 0
soma1 = 0
 
for i in range(0, nProvas):
    print "Digite o peso da", i+1, "o prova: "
    valor = float(input())
    vetPeso.append(valor)
 
for i in range(0, nAlunos):
    print "Digite o", i+1, "o nome: "
    nome = raw_input()
     
    for j in range(0, nProvas):
        print "Digite a", j+1, "o nota do ", nome, ": "
        nota = float(input())
        vetNota.append(nota) 
        soma += nota * vetPeso[i]
    
    vetAlNt.append(vetNota)
    vetNota = []
    print "Media ponderada do aluno:", nome," eh: ", soma/sum(vetPeso)
    soma = 0


for i in range(0, nProvas):
    for j in range(0, nAlunos):
        soma1 +=  vetAlNt[j][i]

    print "A media aritimetica da", i+1, "o prova eh: ", soma1/nAlunos
    soma1 = 0
