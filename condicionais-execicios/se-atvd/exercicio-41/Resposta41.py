num1 = round(float(input("Fale um numero ae meu fi:")))
num2 = round(float(input("Fale outro numero:")))
op = input("Agora fale um operador matematico: + - / * ")
match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "/":
        print(num1 / num2)
    case"*":
        print(num1 * num2)