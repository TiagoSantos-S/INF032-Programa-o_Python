def menu(opcao):
    match opcao:
        case 1:
            print("De Celsius para Fahrenheit")
            cPraF(temperatura)

        case 2:
            print("De Fahrenheit para Celsius")
            fParaC(temperatura)

        case _:
            print("Opção inválida")


def fParaC(temperatura):
    c = (temperatura - 32) * 5 / 9
    print(f"Resultado: {c:.2f} °C")


def cPraF(temperatura):
    f = (temperatura * 9 / 5) + 32
    print(f"Resultado: {f:.2f} °F")


temperatura = float(input("Digite a temperatura: "))
opcao = int(input("Digite sua opção:\n1 - C para F\n2 - F para C\n"))

menu(opcao)