#Armazenando informações de alunos com dicionários
#Criando um dicionário vazio
aluno = {}

#Solicitando ao usuário que insira o nome de um aluno
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

#Solicitando ao usuário que insira o Nota do aluno
nota_final = input("Digite o nota final do aluno: ")
#Adicionando o RA do aluno no dicionário
aluno["nota_final"] = nota_final

#Imprimindo mesagem com as informações do aluno
print(f"O aluno {aluno['nome']}, de {aluno['idade']} anos, do curso de {aluno['curso']} obteve nota final {aluno['nota_final']}")