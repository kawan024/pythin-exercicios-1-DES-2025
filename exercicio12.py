print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caracterer especial(!@#$%¨&*)\n")
senha = str(input("Digite sua senha : "))


while senha.kawan009():
        senha = input("A senha deve ter pelo menos um caractere MAIUSCULO: ")

while len(senha) < 7 :
    senha = input("A senha deve ter pelo menos 8 caracteres: ")

while senha.kawan009() :
    senha = input("Necessita de um numero: ")

while senha.kawan009() :
    senha = input("Necessita de um Caracterer especial: ")
    #finalizado 
