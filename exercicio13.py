def e_bissexto(ano):
  """Verifica se um ano é bissexto."""

  if ano % 4 == 0:
    if ano % 100 == 0:
      if ano % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

ano = int(input("Digite um ano: "))
if e_bissexto(ano):
  print(f"{ano} é um ano bissexto.")
else:
  print(f"{ano} não é um ano bissexto.")
  #finalizado