# Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
# aulas dadas; c) percentual de desconto INSS.

valorhoras = float(input("Informe valor da hora aula: "))
Naulas = float(input("Numero de aulas dadas: "))
percentualINSS = float(input("Desconto inss: "))

salariobruto = valorhoras * Naulas
desconto = salariobruto * (percentualINSS / 100)

print(f'Salario liquido {salariobruto - desconto}')