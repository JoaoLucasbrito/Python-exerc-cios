cor = input("Digite a cor da pulseira de triagem")

if cor == "vermelho": 
    print("Emergência - Atendimento imediato!")
elif cor == "Amarelo":
    print("Urgência - Atendimento rápido.")
elif cor == "Verde":
    print("Pouco urgente - Aguarde sua vez.")
elif cor == "Azul":
    print("Não urgente - Encaminhado para o posto.")
else: 
    print("Cor inválida. Procure a recepção.")