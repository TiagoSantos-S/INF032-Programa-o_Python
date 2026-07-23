entrada = input("Arquivo de entrada: ")
saida = input("Arquivo de saída: ")

vogais = "aeiouAEIOU"

with open(entrada, "r", encoding="utf-8") as arq1, \
     open(saida, "w", encoding="utf-8") as arq2:

    for linha in arq1:
        nova = ""
        for letra in linha:
            if letra in vogais:
                nova += "*"
            else:
                nova += letra
        arq2.write(nova)

print("Arquivo criado.")