valor_total = float(input("Digite o valor total da compra: "))
if valor_total > 150:
    valor_total -= 30
    print("O valor total da compra com desconto é: R$", valor_total)