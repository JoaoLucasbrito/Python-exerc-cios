
cardapio = ["Pastel", "Coxinha", "Refrigerante", "Suco Natural", "Risole", "Bolo (Fatia)"]
codigo = int(input(f"Digite o código do produto:\n1 - Pastel\n2 - Coxinha\n3 - Refrigerante\n4 - Suco Natural\n5 - Risole \n6 - Bolo (Fatia)\n-> "))

match codigo:
    case 1:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case 2:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case 3:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case 4:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case 5:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case 6:
        print(f"Adicionando ao pedido: {cardapio[codigo - 1]}")
    case default:
        print(f"Opção Inválida")