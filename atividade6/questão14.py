litros = float(input("Litros: "))
tipo = input("Combustível (A/G): ").upper()

if tipo == "A":
    preco = 1.90

    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

elif tipo == "G":
    preco = 2.50

    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Tipo inválido.")
    exit()

valor = litros * preco
valor -= valor * desconto

print("Valor a pagar: R$", round(valor, 2))