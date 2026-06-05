# 2.Entrar como nome, idade e sexo de uma pessoa. se a pessoa for do sexo feminino e tiver menos de 25
# anos, imprimir a mensagem (ACEITA), caso contrário, imprimir NAO ACEITA

nome = input("Digite o sseu nome: ")
idade = int(input("Digite a sua idade: "))
sexo = input("Digite o seu sexo com 'feminino' ou 'masculino': ")

if sexo == 'feminino' and idade < 25:
    print("ACEITA")
else:
    print("NAO ACEITA")