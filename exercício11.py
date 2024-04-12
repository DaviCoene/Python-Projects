letra = input("Digite a letra do seu nome: ")

ordeii = ord(letra)
if ordeii > 96:
    letra = chr(ordeii - 32)
    print(letra)
elif ordeii > 64:
    letra = chr(ordeii + 32)
    print(letra)
else:
    print("Inválido: ")

