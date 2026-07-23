arquivo = input("Nome do arquivo: ")

vogais = "aeiouAEIOU"
contador = 0

with open(arquivo, "r", encoding="utf-8") as f:
    for linha in f:
        for letra in linha:
            if letra in vogais:
                contador += 1

print("Quantidade de vogais:", contador)