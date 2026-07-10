# 12. Entrar com dois números inteiros e efetuar a adição. Caso o valor somado seja maior que 20, este
# deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este
# deverá ser apresentado subtraindo-se 5.


numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira o segundo número: "))

soma = numero1 + numero2


if soma > 20:
    soma = soma + 8

else:
    soma = soma - 5

print(f"Resultado final: {soma}")