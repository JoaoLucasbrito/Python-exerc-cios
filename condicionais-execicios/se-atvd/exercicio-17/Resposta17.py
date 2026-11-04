num_reproduções = int(input("Digite o número de reproduções do vídeo: "))
Quantidade_curtidas = int(input("Digite a quantidade de curtidas do vídeo: "))
valor = float(input("Digite o valor ja arrecado pelo vídeo: "))
if num_reproduções > 1000 and Quantidade_curtidas > 200:
    valor += 150
    print(f"Parabéns! O vídeo ganhou 150 reais. O valor total arrecadado é: {valor}")