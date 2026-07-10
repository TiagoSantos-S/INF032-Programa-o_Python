estoque = {
    "teclado": 12,
    "mouse": 5,
    "monitor": 2
}

pendentes = []

while True:
    produto = input("Produto (FIM encerra): ")

    if produto.upper() == "FIM":
        break

    qtd = int(input("Quantidade: "))

    if produto in estoque and estoque[produto] >= qtd:
        estoque[produto] -= qtd
        print("Pedido atendido.")
    else:
        pendentes.append({
            "produto": produto,
            "qtd": qtd
        })
        print("Pedido pendente.")

print("\nEstoque atualizado:")
for produto, qtd in estoque.items():
    print(produto, ":", qtd)

print("\nPedidos pendentes:")
for pedido in pendentes:
    print(pedido["produto"], "-", pedido["qtd"])