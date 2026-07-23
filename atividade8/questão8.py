arquivo1 = input("Primeiro arquivo: ")
arquivo2 = input("Segundo arquivo: ")
arquivo3 = input("Arquivo de saída: ")

with open(arquivo3, "w", encoding="utf-8") as destino:

    with open(arquivo1, "r", encoding="utf-8") as a1:
        destino.write(a1.read())

    with open(arquivo2, "r", encoding="utf-8") as a2:
        destino.write(a2.read())

print("Arquivos unidos.")