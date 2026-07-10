import string

frequencia = {}

while True:
    linha = input("Digite uma linha (Enter vazio encerra): ")

    if linha == "":
        break

    linha = linha.lower()

    for c in ",.;:!?":
        linha = linha.replace(c, "")

    palavras = linha.split()

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

ordenado = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

print("\n5 palavras mais frequentes:")

for palavra, qtd in ordenado[:5]:
    print(palavra, "-", qtd)

print("\nTotal de palavras diferentes:", len(frequencia))