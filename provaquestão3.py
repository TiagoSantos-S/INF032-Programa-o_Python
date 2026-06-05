# Faça um programa que calcule o menor número possível de notas (cédulas) que um valor, 
# inserido pelo usuário, pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 

valor = int(input("insira o valor que deseja sacar\n"))

reserva = valor

qtd100 = 0
qtd50 = 0
qtd20 = 0
qtd10 = 0
qtd5 = 0
qtd2 = 0
qtd1 = 0

while(valor > 0):
    if(valor >= 100):
        valor = valor - 100
        qtd100 += 1
    elif(valor >= 50):
        valor = valor - 50
        qtd50 += 1
    elif(valor >= 20):
        valor = valor - 20
        qtd20 += 1
    elif(valor >= 10):
        valor = valor - 10
        qtd10 += 1
    elif(valor >= 5):
        valor = valor - 5
        qtd5 += 1
    elif(valor >= 2):
        valor = valor - 2
        qtd2 += 1
    else:
        valor -= 1
        qtd1 += 1

print(f"Quantidade de notas necessarias para o troco de {reserva}:\nnotas de 100 {qtd100}\nnotas de 50 {qtd50}\nnotas de 20 {qtd20}\nnotas de 10 {qtd10}\nnotas de 5 {qtd5}\nnotas de 2 {qtd2}\nnotas de 1 {qtd1}")