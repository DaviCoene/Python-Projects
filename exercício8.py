while True:

    valor = int(input("Digite um numero inteiro menor que 1000: "))

    if valor < 1000:
        cent = valor // 100
        dez = (valor //10)-(cent * 10)
        unidade= (valor//1)-(dez*10)-(cent*100)
        print("{} centenas, {} dezenas, {} unidade".format(cent, dez, unidade))
    else:
        print("valor incorreto")

