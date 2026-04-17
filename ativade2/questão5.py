#5. Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km
#com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. Apresentar os
#valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.


tempogasto = float(input("FORNEÇA O TEMPO GASTO (horas): "))
velocidademedia = float(input("FORNEÇA A VELOCIDADE MÉDIA (km/h): "))

distancia = tempogasto * velocidademedia
litros_gastos = distancia / 12

print(f"Velocidade média: {velocidademedia} km/h")
print(f"Tempo gasto: {tempogasto} horas")
print(f"Distância percorrida: {distancia} km")
print(f"Litros gastos: {litros_gastos:.2f} litros")