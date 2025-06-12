def verificar_unidade(unidade):
  """
  Verifica se a unidade do ar está acima do limite (70%).

  Args:
    unidade: Um valor numérico representando a unidade do ar em porcentagem.

  Returns:
    Um string contendo a mensagem de alerta ou uma mensagem informativa.
  """
  if unidade > 70:
    return "ALERTA: Unidade do ar acima do limite (70%)."
  else:
    return "Unidade do ar dentro do limite (70% ou menos)."
  
  unidade = float(input("Digite o valor da unidade do ar em porcentagem: "))
  