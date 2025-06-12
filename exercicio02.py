dias_01 int(input("digite o tempo da tarefa X (em horas): "))
dias_02 int(input("digite o tempo da tarefa Y (em horas): "))
dias_03 int(input("digite o tempo da tarefa Z (em horas): "))

if dias_01 < 0 or dias_02 < 0 or dias_03 < 0:
    print("erro: tempo de tarefa nagativo!")
else:
    total = dias_01 + dias_02 + dias_03 
    print("tempo total para finalizar as tarefas, "horas")
#Finalizado