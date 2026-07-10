total1 = 0
total2 = 0
total3 = 0

cons1 = 0
cons2 = 0

while True:
    numero = int(input("Número do consumidor (0 encerra): "))

    if numero == 0:
        break

    consumo = float(input("Consumo (kWh): "))
    tipo = int(input("Tipo (1-Residencial 2-Comercial 3-Industrial): "))

    if tipo == 1:
        custo = consumo * 0.3
        total1 += consumo
        cons1 += 1

    elif tipo == 2:
        custo = consumo * 0.5
        total2 += consumo
        cons2 += 1

    elif tipo == 3:
        custo = consumo * 0.7
        total3 += consumo

    print("Custo do consumidor: R$", round(custo, 2))

print("\nTotal residencial:", total1)
print("Total comercial:", total2)
print("Total industrial:", total3)

if cons1 > 0:
    print("Média residencial:", total1 / cons1)

if cons2 > 0:
    print("Média comercial:", total2 / cons2)