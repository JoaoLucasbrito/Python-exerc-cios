num1 = int(input("Diga quantas maças vc quer compra?"))

if num1 < 12:
    print(f"O valor total das maças deu:  {num1 * 1.30}")
else:
    print(f"O valor total das maças deu:  {num1 * 1.25}")