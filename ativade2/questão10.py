# 10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
# Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase = "Python é muito legal"

palavra1 = frase[0:6]  
palavra2 = frase[7:8]  
palavra3 = frase[9:14]  
palavra4 = frase[15:20] 

print(palavra1)
print(palavra2)
print(palavra3)
print(palavra4)

print (f"Tamanho da frase: {len(frase)}")
print (f"tamanho da primeira palavra: {len(palavra1)}\nsegunda: {len(palavra2)}\nterceira: {len(palavra3)}\nquarta: {len(palavra4)}")