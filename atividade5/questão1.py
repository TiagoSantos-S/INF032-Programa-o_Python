# 1. que entre com um número e informe se o mesmo está compreendido entre 20 e 90;

num = int(input("Digite um numero: "))

if num > 90 and num < 20:
    print("numero não e compreendido")
else:
    print("numero e compreendido")