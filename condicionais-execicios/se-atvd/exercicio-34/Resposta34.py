idade = int(input("Digite sua idade"))

if idade >= 5 and idade <= 10:
    print("Categoria: Infantil")
elif idade >= 11 and idade <= 14:
    print("Categoria: Juvenil")
elif idade >= 15 and idade <= 17:
    print("Categoria: Cadete")
elif idade >= 18 and idade <= 35:
    print("Categoria: Profissional")
elif idade >= 35:
    print("Categoria: Master")
else:
    print("idade invalida")
