arquivo = input("Nome do arquivo: ")

with open(arquivo, "r", encoding="utf-8") as f:
    linhas = sum(1 for _ in f)

print("Quantidade de linhas:", linhas)