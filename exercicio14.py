valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 500:
    desconto = valor_compra * 0.10
elif valor_compra > 300:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_final = valor_compra - desconto

print("O valor final da compra é: \$", valor_final)
#finalizado