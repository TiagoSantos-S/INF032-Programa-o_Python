# Questão 3 - Avaliação 1 - 2026

nome_completo = input("Digite seu nome completo: ")
nome_usuario = input("Digite seu nome de usuário: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ") 

cadastros = {
    "nome_completo": nome_completo,
    "nome_usuario": nome_usuario,
    "email": email,
    "senha": senha
}

erros = 0
possui_numero = 1
possui_letra = 1

ID = nome_usuario[:3].upper() + str(len(nome_completo))

partes_nome = nome_completo.split()
partes_email = email.split("@")

for num in senha:
    if num <= "9" and num >= "0":
        possui_numero = 0

for char in senha:
    if char >= "A" and char <= "Z" or char >= "a" and char <= "z":
        possui_letra = 0

# Verificar Nome Completo
if nome_completo:
    if len(partes_nome) < 2:
        print("\nCADASTRO INVÁLIDO!")
        print("\n- Nome deve possuir sobrenome.")
        erros += 1

# Verificar Nome de Usuário
if nome_usuario:
    if len(nome_usuario) < 6:
        print("\n- Usuário deve possuir ao menos 6 caracteres.")
        erros += 1
    
    if " " in nome_usuario:
        print("\nNão pode conter espaços.")
        erros += 1
        

# Verificar Senha
if senha:
    if len(senha) < 8:
        print("\n- Senha deve possuir no mínimo 8 caracteres.")
        erros += 1

    if senha == nome_usuario:
        print("\nNão pode ser igual ao usuário.")
        erros += 1

    if possui_numero == 1 or possui_letra == 1:
        print("\nDeve conter pelo menos uma letra e pelo menos um número")
        erros += 1


# Verificar Email
if email:
    if ".com" not in email:
        print("\n- Email deve conter .com.")
        erros += 1

    if "@" not in email:
        print("\n- Email deve conter @.")
        erros += 1

    if "@" in email:
        if len(partes_email[0]) < 3:
            print("\n- O texto antes do @ deve possuir pelo menos 3 caracteres.")
            erros += 1

if erros == 0:
    print("\nCADASTRO VÁLIDO!")
    print(f"ID do usuário: {ID}")

print(f"\nForam encontrados {erros} erros:")
print(f"ID gerado: {ID}")