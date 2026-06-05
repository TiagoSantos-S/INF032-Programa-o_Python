# 8. entrar com o nome, nota 1 e nota 2 de um aluno, imprimir nome, Nota1, nota2, média e a mensagem
# aprovado, reprovado ou em prova final. (a média é 7 para aprovado, 3 para reprovado, e as demais para
# prova final.

nome = (input("Digite seu nome: "))
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Nome - {nome}")
print(f"Nota 1 -{nota1}")
print(f"Nota 2 -{nota2}")
print(f"Media - {media}")

if(media > 7):
    print("Aprovado")
elif(media < 3):
    print("Reprovado")
else:
    print("Prova final")
