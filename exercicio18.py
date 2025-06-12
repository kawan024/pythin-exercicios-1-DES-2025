"""Um professor quer um programa para digitar duas notas e os pesos dessas notas e calcular a média ponderada. 
A média e as notas serão valores do tipo float."""
 
nota1 = float(input("Nota 1:"))
peso1 = float(input("Peso 1:"))
 
nota2 = float(input("Nota 2:"))
peso2 = float(input("Peso 2:"))

media = (nota1*peso1 + nota2*peso2) / (peso1+peso2)
 
print("Média: ",media)
#finalizado