
nome = input("Insira seu nome completo: ")
idade = int(input("Informe sua idade: "))
provatecnica = float(input("Informe a nota da prova técnica: "))
entrevista = float(input("Informe a nota da entrevista: "))

dados_candidato = {
    "nome": nome,
    "idade": idade,
    "prova_tecnica": provatecnica,
    "entrevista": entrevista
}

nomes_separados = dados_candidato["nome"].split()
primeiro_nome = nomes_separados[0]
ultimo_sobrenome = nomes_separados[-1]

login = f"{primeiro_nome.lower()}_{ultimo_sobrenome.lower()}"

caracteres_sem_espaco = len(dados_candidato["nome"].replace(" ", ""))

print(f"\nPrimeiro nome: {primeiro_nome}")
print(f"Último sobrenome: {ultimo_sobrenome}")
print(f"Quantidade de caracteres (sem espaços): {caracteres_sem_espaco}")

if caracteres_sem_espaco < 10:
    print("Alerta: Nome curto!")

pontos = (0.7 * dados_candidato["prova_tecnica"]) + (0.3 * dados_candidato["entrevista"])

if pontos >= 85 and dados_candidato["idade"] >= 18:
    classificacao = "Aprovado"
elif 70 <= pontos < 85 and dados_candidato["idade"] >= 18:
    classificacao = "Banco de Talentos"
else:
    classificacao = "Reprovado"

print("\n")
print(f"Login: {login}")
print(f"Pontuação Final: {pontos:.2f}")
print(f"Classificação: {classificacao}")