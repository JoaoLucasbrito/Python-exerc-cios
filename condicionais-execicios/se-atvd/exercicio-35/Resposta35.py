Turno = input("digitar o turno em que estuda ou trabalha usando apenas uma letra:M (Matutino), V (Vespertino) ou N (Noturno).")

if Turno == "M":
    print("Bom dia!")
elif Turno == "V":
    print("Boa Tarde!")
elif Turno == "N":
    print("Boa noite!")
else:
    print("Turno invalido!")