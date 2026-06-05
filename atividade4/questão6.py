# 6. Dado login = {"user": "dmainart", "nivel": "admin"}, verifique se "user" está em login e se "senha" está em login

login = {"user": "dmainart", "nivel": "admin"}

if "user" in login:
    print("A chave 'user' está em login.")

if "senha" in login:
    print("A chave 'senha' está em login.")
else:
    print("A chave 'senha' não está em login.")
