# Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material radioativo. 
# Sabendo-se que este perde 25% de sua massa a cada 30 segundos, 
# criar um programa que imprima o tempo necessário para que a massa deste material se torne menor que 0,10 gramas. 
# O programa pode calcular o tempo para várias massas. 

tempo = 0

material = float(input("digite o valor do material\n"))

while(material > 0.10):
    material = material - (material / 4)
    tempo += 30

print(f"valor energetico do material {material}\nSeu tempo necessario {tempo}")