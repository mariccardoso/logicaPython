# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))
contador = 0 # Inicializa o contador


# Contagem regressiva até zero
while numero >= 0: # Enquanto o número for maior ou igual que zero (percorre de "numero" até 0)
    print(numero) # Imprime o número
    numero -= 1  # Decrementa o número em 1
    contador += 1 # Incrementa o contador em 1