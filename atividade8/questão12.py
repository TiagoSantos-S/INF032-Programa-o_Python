arquivo = input("Nome do arquivo: ")

with open(arquivo, "w", encoding="utf-8") as arq:

    while True:

        nome = input("Nome: ")
        telefone = input("Telefone (0 encerra): ")

        if telefone == "0":
            break

        arq.write(f"{nome};{telefone}\n")

print("Cadastro salvo.")