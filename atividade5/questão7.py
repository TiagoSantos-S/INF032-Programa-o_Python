# 7.Dada uma lista de cidades e um dicionário que mapeia cada cidade para seu estado (ex.: {"Ouro
# Preto":"MG", "Santos":"SP", ...}), leia uma sigla de estado informada pelo usuário e crie uma
# nova lista apenas com as cidades daquele estado. Se a lista resultante ficar vazia, imprima "nenhuma
# cidade encontrada", senão imprima as cidades em ordem alfabética.

mapeamento = {
    "Ouro Preto": "MG",
    "Santos": "SP",
    "Belo Horizonte": "MG",
    "Campinas": "SP",
    "Salvador": "BA",
    "Tiradentes": "MG"
}


cidades_todas = list(mapeamento.keys())
estado_procurado = input("Digite a sigla do estado: ").upper()

cidades_encontradas = []

def filtrar_cidades(indice):
   
    if indice == len(cidades_todas):
        return 
    
    cidade_atual = cidades_todas[indice]
  
    if mapeamento[cidade_atual] == estado_procurado:
        cidades_encontradas.append(cidade_atual)
 
    filtrar_cidades(indice + 1)

filtrar_cidades(0)

if len(cidades_encontradas) == 0:
    print("nenhuma cidade encontrada")
else:
    cidades_encontradas.sort()
    print(cidades_encontradas)