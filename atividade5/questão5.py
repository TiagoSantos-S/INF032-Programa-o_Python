# 5.Considere um dicionário precos = {"arroz": 22.0, "feijao": 8.5, "carne": 39.9,
# ...} e uma lista de compras ["arroz", "carne", "suco", ...]. Calcule o total somando
# apenas os itens existentes no dicionário. Se o total > 500, aplique 10% de desconto; se estiver entre
# 300 e 500, aplique 5%; caso contrário, sem desconto. Registre também, em uma lista chamada
# indisponiveis, os itens da compra que não estão no dicionário.

precos = {
    "arroz": 22.0, 
    "feijao": 8.5, 
    "carne": 39.9, 
    "suco": 12.0
}

compras = ["arroz", "carne", "suco", "pão", "cerveja"]

total = sum(precos[item] for item in compras if item in precos)

indisponiveis = [item for item in compras if item not in precos]

desconto = 0.0

if total > 500:
    desconto = total * 0.10

if total >= 300:
    if total <= 500:
        desconto = total * 0.05

total_final = total - desconto

print(f"Total Bruto: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total Final: R$ {total_final:.2f}")
print(f"Indisponíveis: {indisponiveis}")