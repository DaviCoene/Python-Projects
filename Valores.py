numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]
for i in numbers:
    maximo = max(numbers)
    print(maximo)
    soma = sum(numbers)
    print(soma)
    quantidade = len(numbers)
    media = soma / quantidade
    print(media)
    numberes = [number for number in numbers if number < 100]
    print(numberes)
