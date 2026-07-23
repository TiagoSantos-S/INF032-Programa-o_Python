def reps(lista):
    repetidos = []

    for elemento in lista:
        if lista.count(elemento) >= 2 and elemento not in repetidos:
            repetidos.append(elemento)

    return repetidos

lista = [1,4,2,3,4,2,3,4]

print(reps(lista))