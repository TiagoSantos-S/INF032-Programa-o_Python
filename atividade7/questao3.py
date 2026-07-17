# 3)Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. 
# Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.

def primo(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


n = int(input("Digite um número: "))

print(f"Números primos de 1 até {n}:")

for i in range(1, n + 1):
    if primo(i):
        print(i)