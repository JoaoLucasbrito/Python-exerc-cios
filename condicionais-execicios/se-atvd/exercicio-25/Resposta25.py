total_alunos = int(input("Digite a quantidade total de alunos: "))
presentes = int(input("Digite a quantidade de alunos presentes: "))
media = float(input("Digite a media da turma: "))

if presentes == total_alunos and media >= 8:
    custo = total_alunos * 5
    print("Custo total das esfihas: R$", custo)
else:
    print("A turma nao atingiu os requisitos para ganhar as esfihas.")