# Faça um programa que recebe uma string do usuário e informa se ela é um palíndromo. Um palíndromo é uma frase que, 
# excluindo os espaços em branco, pode ser lida indiferentemente da esquerda para a direita e da direita para a esquerda. 
# Alguns palíndromos conhecidos são: ovo, radar, a grama é amarga, 
# a base to teto desaba. 

palavra = input("insira sua palavra\n")

palavra = palavra.replace(" ", "")

palavrainversa = palavra[::-1]

if(palavra == palavrainversa):
    print("eh um palidronomo")
else:
    print("não e um palidronomo")