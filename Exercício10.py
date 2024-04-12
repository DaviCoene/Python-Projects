operação = input("Digite uma operação, (+,-,*,/): ")
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if operação == "+":
    print (valor1 + valor2)
elif operação == "-":
    print (valor1 - valor2)
elif operação == "*":
    print (valor1 * valor2)
elif operação == "/":
    if valor2 == 0:
        print("Erro! divisão por zero")
    else:
        print (valor1 / valor2)
else:
    print("Operação inválida")