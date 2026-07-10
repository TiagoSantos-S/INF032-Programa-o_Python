alunos = []

while True:
    nome = input("Nome (FIM encerra): ")

    if nome.upper() == "FIM":
        break

    notas = []

    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    alunos.append({
        "nome": nome,
        "notas": notas
    })

aprovado = 0
recuperacao = 0
reprovado = 0

for aluno in alunos:
    media = sum(aluno["notas"]) / 3

    if media >= 7:
        status = "Aprovado"
        aprovado += 1
    elif media >= 5:
        status = "Recuperação"
        recuperacao += 1
    else:
        status = "Reprovado"
        reprovado += 1

    print(aluno["nome"], "- Média:", round(media, 2), "-", status)

print("\nResumo")
print("Aprovados:", aprovado)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovado)