produtos = []

while True:
    nome = input("Produto: ")
    preco = float(input("Preço (0 para encerrar): "))

    if preco == 0:
        break

    produtos.append({
        "produto": nome,
        "preco": preco
    })

precos = [p["preco"] for p in produtos]

menor = min(precos)
maior = max(precos)
media = sum(precos) / len(precos)

print("\nMenor preço:", menor)
print("Maior preço:", maior)
print("Preço médio:", media)

print("\nProdutos acima da média:")

for p in produtos:
    if p["preco"] > media:
        print(p["produto"], "-", p["preco"])