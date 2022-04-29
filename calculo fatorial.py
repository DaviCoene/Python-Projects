numa = 1
while numa > 0:
    num=int(input("Escolha um número: "))
    num2 = 1
    Resultado = 1 
    while num2 < num:
        num2 += 1
        Resultado *= num2
    print(Resultado)
    numa=int(input("Deseja sair? pressione 0 para sair e 1 para continuar: "))
    
