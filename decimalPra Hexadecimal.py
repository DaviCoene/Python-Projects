q = 0
k = 0
b = 16
valor = []
n = int(input('Qual número você quer converter para Hexadecimal: '))
q = n
while q != 0:
    a = q % b
    if a == 10:
        a = 'A'
    elif a == 11:
        a = 'B'
    elif a == 12:
        a = 'C'
    elif a == 13:
        a = 'D'
    elif a == 14:
        a = 'E'
    elif a == 15:
        a = 'F'
    valor.append(a)
    q = q // b 
    k += 1
newList = [num for num in reversed(valor)]
print(newList)