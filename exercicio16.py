salario = float(input("Digite o seu salário: "))

if salario <= 2000:
    novo_salario = salario * 1.15
elif salario <= 5000:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.05

print(f"O seu novo salário é: R$ {novo_salario:.2f}")
#finalizado