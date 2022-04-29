num = int(input('Insira um numero primo: '))
if num > 1:   
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "isso não é um número primo")
            break
    else:
        print(num, "isso é um número primo")
else:
    print(num, "isso não é um número primo")

