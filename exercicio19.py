def ordenar_numeros():
  """Solicita três números ao usuário e exibe-os em ordem crescente."""

  numeros = []
  for i in range(3):
    while True:
      try:
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
        break
      except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

  numeros.sort() 

  print("\nOs números em ordem crescente são:")
  for numero in numeros:
    print(numero, end=" ")
    #finalizado