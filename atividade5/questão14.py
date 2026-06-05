# 14.Dado um dicionário de aluno como aluno = {"nome": "Ana", "notas": [6.5, 7.0,
# 8.0]}, calcule a média e adicione a chave "status" conforme as regras: média >= 7 → "aprovado",

# média <= 3 → "reprovado", caso contrário → "prova final". Se o aluno tiver alguma nota < 2,
# marque também a chave "atencao": True; caso contrário, "atencao": False.



aluno = {"nome": "Ana", "notas": [6.5, 7.0, 8.0]}


media = sum(aluno["notas"]) / len(aluno["notas"])


if media >= 7:
    aluno["status"] = "aprovado"
elif media <= 3:
    aluno["status"] = "reprovado"
else:
    aluno["status"] = "prova final"


if min(aluno["notas"]) < 2:
    aluno["atencao"] = True
else:
    aluno["atencao"] = False


print(f"Média: {media:.2f}")
print("Dicionário atualizado:", aluno)