entrada = input("Arquivo de entrada: ")
saida = input("Arquivo de saída: ")

dia_atual = int(input("Dia de hoje: "))
mes_atual = int(input("Mês atual: "))
ano_atual = int(input("Ano atual: "))

with open(entrada, "r", encoding="utf-8") as arq1, \
     open(saida, "w", encoding="utf-8") as arq2:

    for linha in arq1:

        dados = linha.split()

        nome = dados[0]
        dia = int(dados[1])
        mes = int(dados[2])
        ano = int(dados[3])

        idade = ano_atual - ano

        if (mes, dia) > (mes_atual, dia_atual):
            idade -= 1

        arq2.write(f"{nome} {idade}\n")

print("Arquivo criado.")