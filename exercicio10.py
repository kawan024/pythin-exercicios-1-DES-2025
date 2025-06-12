salario mensal = float(int(input("digite o salario do mês de renata: "))
parcela_maxima = salario_mês * 0.35

if salario_mês > 3000:
    print("renata tem salario superior a R$ 3.000,00.")
    print("A parcela maxima que ela pode ter é: R$ {parcela_maxima:2f})
else:
    print("O salario do mês de renata é inferior a R$3.000,00.")
    print("Ela não atende ao criterio de salario minimo.")
    #finaizado