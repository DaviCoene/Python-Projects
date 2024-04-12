consumo = int(input("Consumo em Kwh: "))

tipo = input("Tipo da instalação (r, c, i): ")

if tipo == "r":
    if consumo <= 500:
        print("Valor a pagar: {}".format(consumo * 0.4))
    else:
        print("Valor a pagar: {}".format(consumo * 0.65))
elif tipo == "c":
    if consumo <= 1000:
        print("Valor a pagar: {}".format(consumo * 0.55))
    else:
        print("Valor a pagar: {}".format(consumo * 0.60))
elif tipo == "i":
    if consumo <= 5000:
        print("Valor a pagar: {}".format(consumo * 0.55))
    else:
        print("Valor a pagar: {}".format(consumo * 0.60))
else:
    print("Erro! Tipo de instalação desconhecida")