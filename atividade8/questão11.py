arquivo = input("Nome do arquivo: ")

letras = {}

for c in "abcdefghijklmnopqrstuvwxyz":
    letras[c] = 0

caracteres = 0
linhas = 0
palavras = 0

with open(arquivo, "r", encoding="utf-8") as f:

    for linha in f:
        linhas += 1
        caracteres += len(linha)
        palavras += len(linha.split())

        for letra in linha.lower():
            if letra in letras:
                letras[letra] += 1

print("Caracteres:", caracteres)
print("Linhas:", linhas)
print("Palavras:", palavras)

for letra in letras:
    print(letra, ":", letras[letra])