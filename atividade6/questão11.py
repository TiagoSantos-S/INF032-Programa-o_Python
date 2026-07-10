# 11. Dada uma lista de inteiros, separe-os em um dicionário com as chaves "pares" e "impares".
# Se a quantidade de pares for maior que a de ímpares, imprima "mais pares"; caso contrário, imprima
# "mais ímpares". Ao final, mostre também o maior valor de cada grupo (se existir).

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

if(pares > impares):
    print("Mais Pares")
else:
    print("Mais Impares")

maior_par = max(pares)
maior_impar = max(impares)

print("O maior número par eh:", maior_par)
print("O maior número impar eh:", maior_impar)