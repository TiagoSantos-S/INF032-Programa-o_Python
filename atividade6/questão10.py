import math

for i in range(10):

    while True:
        numero = float(input(f"Digite o {i+1}º número positivo: "))

        if numero >= 0:
            break

        print("Número inválido. Digite novamente.")

    print("Raiz quadrada:", math.sqrt(numero))