laboratorios = int(input("Digite a quantidade de laboratorios visitados: "))
pontos = laboratorios * 10

if laboratorios >= 4:
    pontos = pontos + 20

print("Pontuacao final:", pontos)