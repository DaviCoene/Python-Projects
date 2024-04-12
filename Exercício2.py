import math
tempo = int(input("Dìgite o tempo em segundos: "))

constante = tempo / (60*60)
contante2= tempo /60
horas = math.floor((tempo / (60*60)))
min = math.floor((constante - horas) * 60)
min2 = (constante - horas) * 60
segundos = round((min2 - min) * (60))


print("{}h : {}min : {}seg".format(horas, min, segundos))