frutas = ["maçã", "banana", "uva"]
docinhos = ["brigadeiro", "beijinho", "cajuzinho"]
feijoada = ["feijão preto", "carne seca", "linguiça", "costela"]

listona = [frutas, docinhos, feijoada] #----------A

print(listona[1][0]) #----------------------------B

listona[1].append("brigadeiro")
print(docinhos)      #----------------------------C

listona.append("refrigerante")
listona.append("suco")

print(listona)       #----------------------------D