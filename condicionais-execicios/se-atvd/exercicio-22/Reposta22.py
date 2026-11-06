curtidas = int(input("Digite a quantidade de curtidas: "))
comentarios = int(input("Digite a quantidade de comentarios: "))
pontos = int(input("Digite os pontos iniciais: "))

if curtidas >= 100 and comentarios >= 30:
    pontos = pontos + 50

print("Pontuacao final:", pontos)