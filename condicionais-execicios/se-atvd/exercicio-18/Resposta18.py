execucões = int(input("Digite o número de execuções da extesão: "))
num_musicas = int(input("Digite o número de músicas: "))
if execucões >= 10:
    num_musicas += 5
    print(f"Parabéns! Você ganhou 5 músicas extras. O número total de músicas é: {num_musicas}")