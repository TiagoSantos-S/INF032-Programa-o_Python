# 3.Entrar com a sigla do estado de uma pessoa, e imprimir se é carioca, Paulista,
# mineira ou outros estados.

sigla = input("insira a sigla do seu estado: ")

if(sigla == 'SP'):
    print("Paulista")
elif(sigla == 'MG'):
    print("Mineiro")
elif(sigla == 'RJ'):
    print("Carioca")
else:
    print("Outros estados")   