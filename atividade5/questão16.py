# 16. Considere um dicionário de estoque estoque = {"teclado": 12, "mouse": 5,
# "monitor": 2, ...} e uma lista de pedidos de dicionários, por exemplo:
# [{"produto": "mouse", "qtd": 3}, {"produto": "monitor", "qtd": 4}, ...].
# Para cada pedido, se houver quantidade suficiente, baixe do estoque; caso contrário, não altere o
# estoque e registre esse pedido em uma lista pendentes. Ao final, mostre o estoque atualizado e a lista
# de pendentes (vazia ou com itens).

estoque = {
    "teclado": 12, 
    "mouse": 5, 
    "monitor": 2
}

pedidos = [
    {"produto": "mouse", "qtd": 3},      
    {"produto": "monitor", "qtd": 4},    
    {"produto": "teclado", "qtd": 5}    
]

pendentes = []

pedido = pedidos[0]
if pedido["produto"] in estoque:
    if estoque[pedido["produto"]] >= pedido["qtd"]:
        estoque[pedido["produto"]] = estoque[pedido["produto"]] - pedido["qtd"]
    else:
        pendentes.append(pedido)
else:
    pendentes.append(pedido)


pedido = pedidos[1]
if pedido["produto"] in estoque:
    if estoque[pedido["produto"]] >= pedido["qtd"]:
        estoque[pedido["produto"]] = estoque[pedido["produto"]] - pedido["qtd"]
    else:
        pendentes.append(pedido)
else:
    pendentes.append(pedido)


pedido = pedidos[2]
if pedido["produto"] in estoque:
    if estoque[pedido["produto"]] >= pedido["qtd"]:
        estoque[pedido["produto"]] = estoque[pedido["produto"]] - pedido["qtd"]
    else:
        pendentes.append(pedido)
else:
    pendentes.append(pedido)


print("--- ESTOQUE ATUALIZADO ---")
print(estoque)

print("\n--- PEDIDOS PENDENTES ---")
print(pendentes)