valor1 = int(input("Dìgite o primeiro numero"))
valor2 = int(input("Dìgite o segundo numero"))
valor3 = int(input("Dìgite o terceiro numero"))

def max(valor1, valor2, valor3):
    if valor1 > valor2:
        if valor1 > valor3:
            return valor1
        else:
            return valor3
    elif valor2 > valor3:
        if valor2 > valor1:
            return valor2
        else:
            return valor1
    elif valor3 > valor1:
            if valor3 > valor2:
                return valor3
            else:
                return valor2

def min(valor1, valor2, valor3):
    if valor1 < valor2:
        if valor1 < valor3:
            return valor1
        else:
            return valor3
    elif valor2 < valor3:
        if valor2 < valor1:
            return valor2
        else:
            return valor1
    elif valor3 < valor1:
            if valor3 < valor2:
                return valor3
            else:
                return valor2
            
print("O maior número é: {}".format(max(valor1, valor2, valor3)))
print("O menor número é: {}".format(min(valor1, valor2, valor3)))