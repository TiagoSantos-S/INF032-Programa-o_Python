candidatos = {
    1: "Ana",
    2: "Bruno",
    3: "Carla"
}

votos = {1: 0, 2: 0, 3: 0}
invalidos = 0

while True:
    voto = int(input("Vote (0 encerra): "))

    if voto == 0:
        break

    if voto in candidatos:
        votos[voto] += 1
    else:
        invalidos += 1

validos = sum(votos.values())

print("\nResultado:")

for codigo, nome in candidatos.items():
    if validos > 0:
        percentual = votos[codigo] * 100 / validos
    else:
        percentual = 0
    print(f"{nome}: {votos[codigo]} votos ({percentual:.2f}%)")

print("Votos inválidos:", invalidos)

maior = max(votos.values())
vencedores = []

for codigo in votos:
    if votos[codigo] == maior:
        vencedores.append(candidatos[codigo])

if len(vencedores) == 1:
    print("Vencedor:", vencedores[0])
else:
    print("Empate entre:", ", ".join(vencedores))