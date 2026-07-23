def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    return custo + imposto

custo = float(input("Digite o custo do produto: "))
taxa = float(input("Digite a taxa de imposto (%): "))

novo_valor = somaImposto(taxa, custo)

print(f"Valor com imposto: R$ {novo_valor:.2f}")