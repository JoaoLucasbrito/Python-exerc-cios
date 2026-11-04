distancia = float(input("Digite a distância percorrida em km: "))
valor_total = float(input("Digite o valor total da corrida: "))
if distancia >= 10:
    valor_total += 25
    print(valor_total)
    