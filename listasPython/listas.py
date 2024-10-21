# Imprimindo listas

# Criando uma lista
frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi']

# Imprimindo a lista
print(frutas)

#Imprimindo cada elemento da lista
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])

#Solicitando ao usuário para remover um elemento da lista
fruta = input("Digite uma fruta para remover da lista: ")

#Removendo a fruta da lista
frutas.remove(fruta)

#Imprimindo a lista atualizada
print(frutas)