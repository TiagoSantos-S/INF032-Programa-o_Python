tipo = input("Carne (file, alcatra, picanha): ").lower()
kg = float(input("Quantidade (kg): "))
cartao = input("Cartão Tabajara (S/N): ").upper()

if tipo == "file":
    preco = 4.90 if kg <= 5 else 5.80
elif tipo == "alcatra":
    preco = 5.90 if kg <= 5 else 6.80
elif tipo == "picanha":
    preco = 6.90 if kg <= 5 else 7.80
else:
    print("Tipo inválido.")
    exit()

total = preco * kg

if cartao == "S":
    desconto = total * 0.05
else:
    desconto = 0

pagar = total - desconto

print("\n------ CUPOM FISCAL ------")
print("Carne:", tipo)
print("Quantidade:", kg, "kg")
print("Preço total: R$", round(total, 2))
print("Desconto: R$", round(desconto, 2))
print("Valor a pagar: R$", round(pagar, 2))