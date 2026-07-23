def prefixo(palavra1, palavra2):
    return palavra2.startswith(palavra1)

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if prefixo(palavra1, palavra2):
    print("True")
else:
    print("False")