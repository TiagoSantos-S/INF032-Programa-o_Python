arquivo = input("Nome do arquivo: ")

vogais = "aeiouAEIOU"
qtd_vogais = 0
qtd_consoantes = 0

with open(arquivo, "r", encoding="utf-8") as f:
    for linha in f:
        for letra in linha:
            if letra.isalpha():
                if letra in vogais:
                    qtd_vogais += 1
                else:
                    qtd_consoantes += 1

print("Vogais:", qtd_vogais)
print("Consoantes:", qtd_consoantes)