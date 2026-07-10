import math

area = float(input("Área em m²: "))

litros = (area / 6) * 1.10

latas = math(litros / 18)
valor_latas = latas * 80

galoes = math(litros / 3.6)
valor_galoes = galoes * 25

latas_mista = int(litros // 18)
resto = litros - (latas_mista * 18)
galoes_mista = math(resto / 3.6)

valor_misto = (latas_mista * 80) + (galoes_mista * 25)

print("\nApenas latas:")
print(latas, "latas - R$", valor_latas)

print("\nApenas galões:")
print(galoes, "galões - R$", valor_galoes)

print("\nMisturado:")
print(latas_mista, "latas e", galoes_mista, "galões")
print("Valor: R$", valor_misto)