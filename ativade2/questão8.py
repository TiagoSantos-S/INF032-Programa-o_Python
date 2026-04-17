#Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da
#seguinte maneira. Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767.
#Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. O
#ultimo digito desse resultado é o digito verificador da conta (40-> 0 )

numero = int(input("DIGITE UM NUMERO: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10

inverso = unidade * 100 + dezena * 10 + centena

somatotal = numero + inverso

unidade = somatotal % 10
dezena = (somatotal // 10) % 10
centena = (somatotal // 100) % 10

digitoverificador = ((centena * 1) + (dezena * 2) + (unidade * 3) % 10)

print(f'digitoverificador {digitoverificador}')
