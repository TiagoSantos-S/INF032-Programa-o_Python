def perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    return soma == numero

n = int(input("Digite um número: "))

print("Números perfeitos:")

for i in range(1, n + 1):
    if perfeito(i):
        print(i)