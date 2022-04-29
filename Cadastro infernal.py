from datetime import datetime
from re import A
now = datetime.now()
hora = now.hour
minuto = now.minute
senhaadm = 1234
conta=1
if hora>=8 and hora <18:
    print(f'o Horario atual agora é {hora}:{minuto} PERMITIDO o uso do sistema ')
    ADM = int(input("Digite a senha do administador, caso não queira entrar digite 0 : "))
    if ADM == senhaadm :
        cadastro = int(input("deseja criar um cadastro? Digite 1 para não e 0 para Sim: "))
        if cadastro == 0 :
            nome = str(input("Qual seu nome? :"))
            idade = str(input("Qual a sua idade? :"))
            departamento = str(input("Qual seu departamento? :"))
            informaçãoadicional = str(input("Alguma informação adicional?: "))
            contas = int(input("deseja fazer contas de área do quadrado o ou do triangulo? 1 para sim e 0 para Não :"))
            if contas == 1 :
                    while conta >= 1:
                        conta=int(input("Para calcular a área de um Triangulo digite: 1 ,ou de quadrado digite 2,"))
                        if conta == 1:
                            h = int(input("qual seu valor da altura?: "))
                            y = int(input("qual o valor da base?: "))
                            triangulo = (h*y)/2
                            print("o valor a area do tringulo é : ", triangulo)
                            conta=int(input("deseja sair digite 0, caso contrário digite 1: "))
                        else:
                            a = int(input("Qual o valor da base?"))
                            b = a * a 
                            print ("o valor da area do quadrado é:", b)
                            conta=int(input("deseja sair digite 0, caso contrário digite 1: ")) 
            else: 
                print("Obrigado por usar nosso sistema :)")     
        else: 
            print("Obrigado por usar nosso sistema :)") 
    else: 
        print("Obrigado por usar nosso sistema :)")                             
else:
    print(f'O Horario atula agora é {hora}:{minuto} NÃO PERMITIDO o uso do sistema')
