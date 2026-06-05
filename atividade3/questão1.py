#questão 1.

Lista1 = [1,5,3,6,5,6,7,7,10]
print(Lista1)

#questão 1.2

print(Lista1[0])
print(Lista1[4])
print(Lista1[8])

#questão 1.3

Lista1[0] = 9

print(Lista1)

#questão 1.4

numero1 = int(input("Digite um numero: "))

Lista1.append(numero1)

print(Lista1)

#questão 1.5

del Lista1[9]

print(Lista1)

#questão 1.6

print(len(Lista1))

#questão 1.7

soma = sum(Lista1)

print(soma)

#questão 1.8

Lista = [1,5,3,4,22,6,7,11,10]

Lista.sort()

print(Lista)

#questão 1.9

Lista1.reverse()

print(Lista1)

#questão 1.10

Lista1 = [1,5,3,6,5,6,7,7,10]

print(Lista1.count(7)) 

#questão 1.11

Listafatiada = Lista1[3:8]

print(Listafatiada)

#questão 1.12

Lista1 = [1, 2, 5, 4, 9]
Lista2 = [3, 2, 5, 7, 8]

Lista3 = Lista1 + Lista2

print(Lista3)

#questão 1.13

numero1 = int(input("Digite um numero: "))

if numero1 in Lista1:
    print(f"True")
else:
    print(f"False")

#questão 1.14

lista = [1, 2, 2, 3, 4, 1]
lista_unica = list(set(lista))


