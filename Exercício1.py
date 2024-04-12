nomeCompleto = input("Insira seu nome completo com letras minúsculas: ")
print(nomeCompleto.title())
letras = len(nomeCompleto) - nomeCompleto.count(" ")
print("seu nome possui {} caracteres".format(letras));
