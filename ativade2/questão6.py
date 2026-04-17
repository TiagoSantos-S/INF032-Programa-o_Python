# 6. Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
# calcule o valor da prestação.

emprestimo = float(input("Digite o valor do emprestimo: "))
taxaJuros = float(input("Digite o valor da taxa de juros: ")) / 100
qtdMeses = int(input("Digite a quantidade de meses: "))

valorPrestacao =  emprestimo * (taxaJuros * (1 + taxaJuros) ** qtdMeses) / ((1 + taxaJuros) ** qtdMeses - 1)

print(f"Valor das prestações : {valorPrestacao:.2f}")
