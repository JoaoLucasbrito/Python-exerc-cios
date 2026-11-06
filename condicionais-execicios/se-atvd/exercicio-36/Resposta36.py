gol1 = int(input("Digite a quantidade de gols que o time A fez:"))
gol2 = int(input("Digite a quantidade de gols que o time B fez:"))

if gol1 > gol2:
    print("vitoria do time A")
elif gol2 > gol1:
    print("Vitoria do time B")
else: 
    print("empatou infelizmente!")