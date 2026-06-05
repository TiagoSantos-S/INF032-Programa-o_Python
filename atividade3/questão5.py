

lista = [
    "arroz", "feijão", "macarrão", "óleo", "leite", "ovos", "pão",
    "frutas", "verduras", "carne",
    "sabão em pó", "detergente", "desinfetante", "água sanitária",
    "sorvete"
]


print("Lista inicial:")
print(lista)

produtos_limpeza = ["sabão em pó", "detergente", "desinfetante", "água sanitária"]



lista = list(set(lista) - set(produtos_limpeza))


print("\nApós ir ao mercado (sem produtos de limpeza):")
print(lista)


if "sorvete" in lista:
    lista.remove("sorvete")


print("\nApós ir à sorveteria (sem sorvete):")
print(lista)