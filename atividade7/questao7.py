def contar_letra(texto, letra):
    return texto.count(letra)

texto = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

print(f"A letra '{letra}' aparece {contar_letra(texto, letra)} vez(es).")