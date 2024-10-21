# Solicita um número ao usuário
numero = int(input("Digite um número: "))
contador = 0

# Enquanto o número for positivo, solicita outro número
while numero >= 0:
    contador += 1 # Incrementa o contador em 1
    numero = int(input("Digite um número: ")) # Solicita outro número

print("Você digitou", contador, "números positivos.") # Imprime a quantidade de números positivos digitados

