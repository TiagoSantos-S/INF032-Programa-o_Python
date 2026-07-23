arquivo = input("Nome do arquivo: ")
palavra = input("Palavra: ")

contador = 0

with open(arquivo, "r", encoding="utf-8") as f:
    for linha in f:
        palavras = linha.split()
        contador += palavras.count(palavra)

print("Quantidade:", contador)