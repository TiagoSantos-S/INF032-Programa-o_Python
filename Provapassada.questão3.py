nomecompleto = input("Nome: ")
nomeusuario = input("Usuário: ")
senha = input("Senha: ")
e_mail = input("Email: ")

Dados_login = {
    "nome_completo": nomecompleto,
    "nome_usuário": nomeusuario,
    "senha": senha,
    "e_mail": e_mail,
}

ID = Dados_login["nome_usuário"][:3].upper() + str(len(Dados_login["nome_completo"]))

lista_erros = []

nomedividido = Dados_login["nome_completo"].split()
if(len(nomedividido) < 2):
    lista_erros.append("- Nome deve possuir sobrenome.\n")

usuario_sem_espaco = len(Dados_login["nome_usuário"])
tem_espaco = False
icont = 0

while(usuario_sem_espaco > icont):
    if(Dados_login["nome_usuário"][icont] == " "):
        tem_espaco = True
    icont = icont + 1

if(usuario_sem_espaco < 6 or tem_espaco):
    lista_erros.append("- Usuário deve possuir ao menos 6 caracteres.")

# 3. VALIDAÇÃO DA SENHA (Usando o seu while e variáveis de acertos)
acertos1 = 0 # Para números
acerto2 = 0  # Para letras
icont = 0

while(len(Dados_login["senha"]) > icont):
    # Checando número (igual você fez)
    if(Dados_login["senha"][icont] == '1' or Dados_login["senha"][icont] == '2' or Dados_login["senha"][icont] == '3' or Dados_login["senha"][icont] == '4' or Dados_login["senha"][icont] == '5' or Dados_login["senha"][icont] == '6' or Dados_login["senha"][icont] == '7' or Dados_login["senha"][icont] == '8' or Dados_login["senha"][icont] == '9' or Dados_login["senha"][icont] == '0'):
        acertos1 = 1
    
    # Checando letra
    if(Dados_login["senha"][icont].isalpha()):
        acerto2 = 1
        
    icont = icont + 1

# Valida todas as regras da senha juntas
if(len(Dados_login["senha"]) < 8 or acertos1 == 0 or acerto2 == 0 or Dados_login["senha"] == Dados_login["nome_usuário"]):
    lista_erros.append("- Senha deve possuir no minimo 8 caracteres.")

# 4. VALIDAÇÃO DO EMAIL (Usando o seu while e acertogmail)
acertogmail = 0
tem_arroba = 0
icont = 0

# Se os últimos 4 caracteres forem .com
if(Dados_login["e_mail"][-4:] == '.com'):
    acertogmail = 1

while(len(Dados_login["e_mail"]) > icont):
    if(Dados_login["e_mail"][icont] == '@'):
        # Para ter 3 caracteres ANTES do @, o @ precisa estar no mínimo na posição 3 (índices 0, 1 e 2)
        if(icont >= 3):
            tem_arroba = 1
    icont = icont + 1

if(acertogmail == 0 or tem_arroba == 0):
    lista_erros.append("- Email deve conter .com.")

# --- SAÍDA FORMATADA EXATAMENTE COMO A PROVA ---
print("\n")
if(len(lista_erros) == 0):
    print("CADASTRO VÁLIDO")
else:
    print("CADASTRO INVÁLIDO")
    print(f"Foram encontrados {len(lista_erros)} erros:")
    
    # Imprime os textos que guardamos na lista
    for erro in lista_erros:
        print(erro)

print(f"ID GERADO: {ID}")