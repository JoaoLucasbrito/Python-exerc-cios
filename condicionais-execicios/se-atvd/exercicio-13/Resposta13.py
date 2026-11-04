pontos = int(input("Digite a quantidade de pontos: "))
jogos_comprados = int(input("Digite a quantidade de jogos comprados: "))
valor_total = float(input("Digite o valor total da compra: "))

if jogos_comprados >= 3 and valor_total > 500:
    pontos += 200
    print("Parabéns! Você ganhou 200 pontos extras!")