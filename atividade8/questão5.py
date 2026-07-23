arquivo = input("Nome do arquivo: ")

contador = {}

for letra in "abcdefghijklmnopqrstuvwxyz":
    contador[letra] = 0

with open(arquivo, "r", encoding="utf-8") as f:
    for linha in f:
        for letra in linha.lower():
            if letra in contador:
                contador[letra] += 1

for letra in contador:
    print(letra, ":", contador[letra])