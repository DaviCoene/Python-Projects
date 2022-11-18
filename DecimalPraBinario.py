q = 0
k = 0
b = 2
valor = []
n = int(input('Qual número você quer converter para binario?: '))
q = n
while q != 0:
    a = q % b
    valor.append(a)
    q = q // b 
    k += 1
newList = [num for num in reversed(valor)]
print(newList)
    

