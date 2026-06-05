# 6.entrar com 3 números e imprimi-los em ordem crescente

num1 = int (input("digite o primeiro numero"))
num2 = int (input("digite o segundo numero"))
num3 = int (input("digite o terceiro numero"))

if(num1 < num2 and num1 < num3):
    menornumero = num1
elif(num2 < num1 and num2 < num3):
    menornumero = num2
elif(num3 < num1 and num3 < num2):
    menornumero = num3

if(num1 > num2 and num1 > num3):
    maiornumero = num1
elif(num2 > num1 and num2 > num3):
    maiornumero = num2
elif(num3 > num1 and num3 > num2):
    maiornumero = num3     

if(num1 > menornumero and num1 < maiornumero):
    meio = num1
elif(num2 > menornumero and num2 < maiornumero):
    meio = num2
elif(num3 > menornumero and num3 < maiornumero):
    meio = num3


print(f"{menornumero},{meio},{maiornumero}")    