Livros = int(input("Digite a quantidade de livros: "))
Jogos = int(input("Digite a quantidade de jogos: "))
valor_total = float(input("Digite o valor total da compra: "))
if Livros >= 2 and Jogos >= 3:
    valor_total -= 25
    print(f"Parabéns! Você ganhou 25 reais de desconto. O valor total da compra com desconto é: R$ {valor_total}")
