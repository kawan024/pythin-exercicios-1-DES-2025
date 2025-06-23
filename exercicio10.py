salário mensal = float(int(input("digite o salário do mês de renata: "))
parcela_maxima = salário_mês * 0.35

if salário_mês > 3000:
    print("renata tem salario superior a R$ 3.000,00.")
    print("A parcela maxima que ela pode ter é: R$ {parcela_maxima:2f})
else:
    print("O salário do mês de renata é inferior a R$3.000,00.")
    print("Ela não atende ao criterio de salário minimo.")
    #finaizado