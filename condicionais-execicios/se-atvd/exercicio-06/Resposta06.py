valor_tranferencia = float(input("Digite o valor da transferência: "))
if valor_tranferencia > 1000:
    valor_tranferencia -= 15
print(f"O valor da transferência é: {valor_tranferencia}")