# 1. Entrar com dois números inteiros e imprimir a seguinte saída: a)dividendo; b) divisor; c) quociente; d) resto.


numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite o segundo numero: "))

print(f'Dividendo : {numero1}')
print(f'Divisor : {numero2}')
print(f'Quociente : {numero1 * numero2}')
print(f'Resto : {numero1 % numero2}')