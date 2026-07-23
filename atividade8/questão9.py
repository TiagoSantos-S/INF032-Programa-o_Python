entrada = input("Arquivo de entrada: ")
saida = input("Arquivo de saída: ")

maior_cidade = ""
maior_pop = 0

with open(entrada, "r", encoding="utf-8") as arq:

    for linha in arq:
        dados = linha.split()

        cidade = " ".join(dados[:-1])
        habitantes = int(dados[-1])

        if habitantes > maior_pop:
            maior_pop = habitantes
            maior_cidade = cidade

with open(saida, "w", encoding="utf-8") as arq:
    arq.write(f"{maior_cidade} {maior_pop}")

print("Arquivo criado.")