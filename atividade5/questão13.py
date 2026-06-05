# 13. Entrar com um número e escrever uma das mensagens: “é múltiplo de 3", ou "não é múltiplo de 3

numero = int(input("Informe o numero: "))

if numero % 3 == 0:
    print("Eh divisivel por 3")
else:
    print("Nao eh divisivel por 3")