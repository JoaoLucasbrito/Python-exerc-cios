situação = input("o cliente esta cadastrado? (S/N)")
cidade = input("Qual a sua cidade de origem?")

if situação == "S":
    if cidade == "Emtupi":
        print("entrega libeirada!")
    else:
        print("vai para analise logistica")
elif situação == "N":
    if cidade == "Emtupi":
        print("solicitar cadastro antes de entregar")
    else:
        print("entrega não permitida.")
else:
   ("erro ao digitando")
