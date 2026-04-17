# 2. Entrar com quatro números e imprimir a media ponderada, sabendo-se que os pesos são respectivamente 1,2,3,4.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terceiro numero: "))
numero4 = int(input("digite o quarto numero: "))

multitotal = (numero1 * 1) + (numero2 * 2) + (numero3 * 3) + (numero4 * 4)
somapesos = 1 + 2 + 3 + 4

print(f'Media ponderada: {multitotal / somapesos}')