#Criar um programa que leia a quantidade de fotas de uma locadora de vídeo possui e o valor que ela cobra
#por cada aluguel, mostrando as informações pedidas a seguir: a) sabendo que um terço das fitas são
#alugadas por mês, exiba o faturamento anual da locadora; b)Quando o cliente atrasa a entrega, é cobrada
#uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
#devolvidas com atraso, calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se
#estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
#que a locadora terá no final do ano.

qtdFitas = int(input("Digite a quantidade de fitas: "))
valorAluguel = float(input("Digite o valor do aluguel por fita: "))


fitasAlugadasMes = qtdFitas / 3
faturamentoMensal = fitasAlugadasMes * valorAluguel
faturamentoAnual = faturamentoMensal * 12


fitasAtrasadas = fitasAlugadasMes / 10
valorMultaPorFita = valorAluguel * 0.10
valorMultasMes = fitasAtrasadas * valorMultaPorFita


fitasEstragadas = qtdFitas * 0.02
fitasCompradas = qtdFitas / 10
qtdFinalFitas = qtdFitas - fitasEstragadas + fitasCompradas


print(f"\nFaturamento anual: R$ {faturamentoAnual:.2f}")
print(f"Valor ganho com multas por mês: R$ {valorMultasMes:.2f}")
print(f"Quantidade de fitas ao final do ano: {int(qtdFinalFitas)}")