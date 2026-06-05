# 9. Com perfil = {"nome": "Ivo", "cidade": "Salvador"}, use update() para adicionar "idade": 30 e
# alterar "cidade" para "Feira de Santana". Verifique o resultado.

perfil = {"nome": "Ivo", "cidade": "Salvador"}
print(perfil)

perfil.update({"idade": 30})
perfil.update({"cidade": "Feira de Santana"})
print(perfil)