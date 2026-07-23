arquivo = input("Nome do arquivo: ")
caractere = input("Caractere: ")

contador = 0

with open(arquivo, "r", encoding="utf-8") as f:
    for linha in f:
        contador += linha.count(caractere)

print("Ocorrências:", contador)