# Solicita ao usuário que insira um número
numero = int(input("Digite um número: 60"))

# Verifica se o número é positivo, negativo ou zero
if numero > 0: # Se o número for maior que zero
    print("O número é positivo.")
elif numero < 0: # Se o número for menor que zero
    print("O número é negativo.")
else:
    print("O número é zero.")  # Se o número for igual a zero