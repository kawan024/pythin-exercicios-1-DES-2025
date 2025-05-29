peso = float(input("digite o peso (kg): "))
altura = float(input("digite a altura (m): "))

imc = peso / (altura ** 2 )

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso.")
elif imc < 25:
    print("peso normal.")
else:
    print("acima do peso.")