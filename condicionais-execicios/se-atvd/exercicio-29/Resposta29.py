ano = int(input("Digite seu ano de nascimento: "))
if ano - 2026 >= 18:
    print("Você é obrigado a votar")
elif ano - 2026 >= 16:
    print("Você não é obrigado a votar")
elif ano - 2026 >= 70:
    print("Você não é obrigado a votar")
elif ano - 2026 < 16:
    print("Você não pode votar")
else:
    print("Você não é obrigado a votar")