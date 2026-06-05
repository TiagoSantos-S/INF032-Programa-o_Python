# 15.A prefeitura do Rio de Janeiro abriu uma linha de crédito para seus funcionários. O valor máximo da
# prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o
# salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.



salario_bruto = float(input("Digite o valor do salário bruto: R$ "))
valor_prestacao = float(input("Digite o valor da prestação desejada: R$ "))

limite_prestacao = salario_bruto * 0.30

if valor_prestacao <= limite_prestacao:
    print("Empréstimo CONCEDIDO.")
else:
    print("Empréstimo NÃO CONCEDIDO. O valor da prestação ultrapassa 30% do salário bruto.")