mikaelly_dinheiro = float(input("Digite o valor do dinheiro que Mikaelly possui: "))
ingresso = float(input("Digite o valor do ingresso: "))
passagem = float(input("Digite o valor da passagem: "))
if mikaelly_dinheiro >= ingresso + passagem:
    mikaelly_dinheiro += 100
    print(f"Parabéns! Mikaelly ganhou 100 reais. Seu novo saldo é: {mikaelly_dinheiro}")