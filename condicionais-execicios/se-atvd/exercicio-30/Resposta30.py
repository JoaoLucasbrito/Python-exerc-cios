# receber 2 valores e saber qual é o maior ou se são iguais
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
if num1 > num2:
    print(f"O numero {num1} é maior que o numero {num2}")   
elif num2 > num1:
    print(f"O numero {num2} é maior que o numero {num1}")
else:
    print(f"Os numeros {num1} e {num2} são iguais")