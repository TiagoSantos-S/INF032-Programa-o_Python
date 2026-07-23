entrada = input("Arquivo de entrada: ")
saida = input("Arquivo de saída: ")

with open(entrada, "r", encoding="utf-8") as arq1, \
     open(saida, "w", encoding="utf-8") as arq2:

    for linha in arq1:
        arq2.write(linha.upper())

print("Arquivo criado.")