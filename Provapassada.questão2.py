valores = []
produto = []

icont = 0 

while(icont < 5):
    valor_digitado = float(input("Informe o valor do seu produto: "))
    valores.append(valor_digitado)
    
    nome_digitado = input("Informe o nome do seu produto: ")
    produto.append(nome_digitado)
    
    icont += 1 

indice_menor = 0
indice_maior = 0
faturamento = valores[0]
menor = valores[0]
maior = valores[0]

icont = 1 

while(icont < 5):
    faturamento += valores[icont]

    if(valores[icont] < menor):
        menor = valores[icont]
        indice_menor = icont

    if(valores[icont] > maior):
        maior = valores[icont]
        indice_maior = icont
        
    icont += 1

ticket_medio = faturamento / 5

print(f'\nFaturamento: R$ {faturamento:.2f}')
print(f'Ticket médio: R$ {ticket_medio:.2f}')
print(f'Maior venda: {produto[indice_maior]}')
print(f'Menor venda: {produto[indice_menor]}')

if ticket_medio >= 1200 and faturamento >= 6000:
    print('Desempenho: Excelente')
elif ticket_medio >= 700 and faturamento >= 3500:
    print('Desempenho: Bom')
else:
    print('Desempenho: Regular')

if maior > (0.4 * faturamento):
    print('Atenção: concentração excessiva de receita.')