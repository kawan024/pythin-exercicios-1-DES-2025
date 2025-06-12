alunos = ["alice", "bruno", "carla"]
dias = [ "seg", "ter", "qua", "qui"]

reservas = [["ausente" for _ in dias} for _ in alunos]

print("preencha" com 'S' para preencha e 'x' para ausencia:")
      
for i, aluno enumerate(alunos):
    print(f"\nAlunos: {alunos}")
    for j, dia in enumerate(dias):
        entrada = input(f" {dia}: ")
        if entrada.upper() == 'S' :
            reservas[i][j] = "presente"
      

    print("\nTabela de reservas:")
    print(f"{'aluno: <10} {' '.join(f'{d:<10}' for d in dias])}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '. join([f'{res;<10}' for res in reservas[i]])}")
    