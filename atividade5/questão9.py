# 9.Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
# menor que 20,00, caso contrário o lucro será de 30%. entrar com o valor do produto e imprimir o valor da
# venda.

produto = float(input("insira o valor do produto: "))

if(produto < 20):
    produto = produto + (produto * 0.30)
else:
    produto = produto + (produto * 0.45)


print(f"valor da venda {produto}")        