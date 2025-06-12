consumo_total = float(input("digite o consumo total de internet (em GB): "))

limite = 100

if consumo_total > limite:
    print(f"0 consumo de {consumo_total} GB excede o limite de {limite} GB.")
else:
    print(f"0 consumo de {consumo_total} GB está dentro do limite de {limite} GB.")
    #finalizado