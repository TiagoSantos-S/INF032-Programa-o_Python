peso = float(input("Peso dos peixes (kg): "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print("Peso:", peso)
print("Excesso:", excesso)
print("Multa: R$", multa)