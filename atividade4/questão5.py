# 5. Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome,
# idade, telefone. O programa deve ler um 5 dados completos, e imprimir todos os itens do
# dicionário no formato chave: nome-idade-fone.


agenda = {
    "11111111111": {
        "nome": "Ana",
        "idade": 20,
        "telefone": "7199999-1111"
    },

    "22222222222": {
        "nome": "Bruno",
        "idade": 25,
        "telefone": "7199999-2222"
    },

    "33333333333": {
        "nome": "Carlos",
        "idade": 30,
        "telefone": "7199999-3333"
    },

    "44444444444": {
        "nome": "Daniela",
        "idade": 22,
        "telefone": "7199999-4444"
    },

    "55555555555": {
        "nome": "Eduardo",
        "idade": 28,
        "telefone": "7199999-5555"
    }
}

print(f"11111111111: {agenda['11111111111']['nome']}-{agenda['11111111111']['idade']}-{agenda['11111111111']['telefone']}")

print(f"22222222222: {agenda['22222222222']['nome']}-{agenda['22222222222']['idade']}-{agenda['22222222222']['telefone']}")

print(f"33333333333: {agenda['33333333333']['nome']}-{agenda['33333333333']['idade']}-{agenda['33333333333']['telefone']}")

print(f"44444444444: {agenda['44444444444']['nome']}-{agenda['44444444444']['idade']}-{agenda['44444444444']['telefone']}")

print(f"55555555555: {agenda['55555555555']['nome']}-{agenda['55555555555']['idade']}-{agenda['55555555555']['telefone']}")