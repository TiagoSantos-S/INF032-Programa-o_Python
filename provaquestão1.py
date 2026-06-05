# Sabendo-se que a UAL calcula a divisão através de subtrações sucessivas, 
# criar m programa que calcule e imprima o resto da divisão de números inteiros lidos. 
# suponha que os números lidos sejam positivos e que o dividendo seja maior que o divisor. 


dividendo = int(input("escolha o numero que deseja dividir\n"))
divisor = int(input("escolha por quanto deseja dividir\n"))

while(dividendo >= divisor):
    dividendo = dividendo - divisor

print(f"O resto da divisão = {dividendo}")