#programa de lista de dicionarios alunos
#Criando uma lista vazia para armazenar os alunos
alunos = []

#Criando um loop para solicitar informações de alunos
while True: 
    #Criando um dicionário vazio para armazenar as informações do aluno
    aluno = {}

    #Solicitando ao usuário que insira o nome do aluno
    nome = input("Digite o nome do aluno: ")
    #Adicionando o nome do aluno no dicionário
    aluno["nome"] = nome

    #Solicitando ao usuário que insira a idade do aluno
    idade = int(input("Digite a idade do aluno: "))
    #Adicionando a idade do aluno no dicionário
    aluno["idade"] = idade

    #Solicitando ao usuário que insira o curso do aluno
    curso = input("Digite o curso do aluno: ")
    #Adicionando o curso do aluno no dicionário
    aluno["curso"] = curso

    #Solicitando ao usuário que insira o RA do aluno
    ra = input("Digite o RA do aluno: ")
    #Adicionando o RA do aluno no dicionário
    aluno["ra"] = ra

    #Adicionando o dicionário do aluno na lista de alunos
    alunos.append(aluno)

    #Solicitando ao usuário se deseja adicionar mais um aluno
    continuar = input("Deseja adicionar mais um aluno? (s/n): ")
    if continuar.lower() == "n":
        break

#Imprimindo a lista de alunos
print("Lista de alunos:")
for aluno in alunos:
    print(f"O aluno {aluno['nome']}, de {aluno['idade']} anos, do curso de {aluno['curso']} com RA {aluno['ra']}")

#Média das notas dos alunos
soma = 0
for aluno in alunos:
    soma += aluno["nota_final"]

media = soma / len(alunos)
print(f"A média das notas dos alunos é {media}")