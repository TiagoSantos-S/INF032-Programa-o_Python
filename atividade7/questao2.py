# 2) A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. 
# O termo seguinte da sequência é obtido somando os dois anteriores. Faça uma script em Python que solicite um inteiro positivo ao usuário, 
# n. Então uma função exibe todos os termos da sequência até o n-ésimo termo. Use recursividade.

def fibonacci(n, atual=0, proximo=1, contador=1):
    if contador > n:
        return

    print(atual)

    fibonacci(n, proximo, atual + proximo, contador + 1)


num = int(input("Digite o número de termos: "))
fibonacci(num)

