cargo = input("Qual o seu cargo? (func ou admin)")
tempo_empresa = int(input("Qual o seu tempo de empresa?"))

if cargo == "admin":
  if tempo_empresa >= 5:
    print("Pode receber promoção:")
  else:
    print("Ainda não esta apto para receber promoção")
elif cargo == "func":
   if tempo_empresa >= 3:
      print("Pode receber promoção:")
   else:
      print("Ainda não esta apto para receber promoção")
else:
   ("Cargo invalido, erro ao digitando")
