from random import choice
from time import sleep
import json
A = input("Esse Aplicativo será para organizar seu orçamento para que pare de gastar atoa: pressione Enter para continuar: ")
##Frases para colocar em momentos do aplicativo
frases = ["a vontade é momentanea, o dinheiro não{ ... }","se você não comprar nada o desconto é maior{ julios }", "muitos gastam dinheiro que ainda não ganham, comprando coisas de que não precisam para impressionar pessoas de quem não gostam{Will Smith}" , "cuidado com as pequenas despesas, um pequeno vazamento afundará um grande navio", "se queres saber o valor do dinheiro, tenta pedi-lo emprestado", "regra nº1 nunca perca dinheiro, regra nº2 nunca se esqueça da regra nº1"]
##Escolha das frases
def my_fucion():
    print(choice(frases))
##Para evitar erros de digitação errada
def gum():
    amp = int(input("caso deseje fazer seu orçamento mensal digite 2, para anual 1, ou diario digite 0: "))
##Programa Funcionando para uso mensal
def din ():
    print(choice(frases))
    print("Carregando...")
    sleep(5)
    A = input("Esse Aplicativo será para organizar seu orçamento Mensal para que pare de gastar atoa: pressione Enter para continuar: ")
    Dinheiro = int(input("Quanto você pode gastar?:"))
    Ja = 1
    Kl = 1
    L,C = [] , []
    while Kl > 0:
        Aj = input("Digite o item que você comprou: ")
        Ja = float(input("Indique o valor deste item: "))
        Kl= int(input("Tem mais compras: Digite 1 para sim, e 0 para não: "))
        L.append(Ja)
        C.append(Aj)    
    for i in range(len(L)):
        print(f"Item :{C[i]} Valor:{L[i]} ")
    soma= sum(L)
    L.sort()
    L.reverse()
    print("Ordem das coisas mais caras as mais baratas que você comprou: ", L)
    print("Você ja gastou:", soma)
    L.append(0)
    L.sort()
    print('Ordem das coisas mais baratas as mais caras', L)
    print("Maior dinheiro gasto em um item:", max(L))
    print("Menor dinheiro gasto em um item:", L[0])
    a = Dinheiro - soma
    if a < 1:
        print("Você está gastando demais")
        my_fucion()
    print("Seu saldo esse mês:", a)
    return(A, Dinheiro, Ja, L,C,i,soma,a)
##Programa Funcionando para uso anual
def din1():
    print(choice(frases))
    print("Carregando...")
    sleep(5)
    A = input("Esse Aplicativo será para organizar seu orçamento anual para que pare de gastar atoa: pressione Enter para continuar: ")
    Dinheiro = int(input("Quanto você pode gastar?:"))
    Ja = 1
    Kl = 1
    L,C = [] , []
    while Kl > 0:
        Aj = input("Digite o item que você comprou: ")
        Ja = float(input("Indique o valor deste item: "))
        Kl= int(input("Tem mais compras: Digite 1 para sim, e 0 para não: "))
        L.append(Ja)
        C.append(Aj)    
    for i in range(len(L)):
        print(f"Item :{C[i]} Valor:{L[i]} ")
    soma= sum(L)
    L.sort()
    L.reverse()
    print("Ordem das coisas mais caras as mais baratas que você comprou: ", L)
    print("Você ja gastou:", soma)
    L.append(0)
    L.sort()
    print('Ordem das coisas mais baratas as mais caras', L)
    print("Maior dinheiro gasto em um item:", max(L))
    print("Menor dinheiro gasto em um item:", L[0])
    a = Dinheiro - soma
    if a < 1:
        print("Você está gastando demais")
        my_fucion()
    print("Seu saldo esse ano:", a)
    return(A, Dinheiro, Ja, L,C,i,soma,a)
##Programa Funcionando para uso Diario
def din2():
    print(choice(frases))
    print("Carregando...")
    sleep(5)
    A = input("Esse Aplicativo será para organizar seu orçamento diario para que pare de gastar atoa: pressione Enter para continuar: ")
    Dinheiro = int(input("Quanto você pode gastar?:"))
    Ja = 1
    Kl = 1
    L,C = [] , []
    while Kl > 0:
        Aj = input("Digite o item que você comprou: ")
        Ja = float(input("Indique o valor deste item: "))
        Kl= int(input("Tem mais compras: Digite 1 para sim, e 0 para não: "))
        L.append(Ja)
        C.append(Aj)    
    for i in range(len(L)):
        print(f"Item :{C[i]} Valor:{L[i]} ")
    soma= sum(L)
    L.sort()
    L.reverse()
    print("Ordem das coisas mais caras as mais baratas que você comprou: ", L)
    print("Você ja gastou:", soma)
    L.append(0)
    L.sort()
    print('Ordem das coisas mais baratas as mais caras', L)
    print("Maior dinheiro gasto em um item:", max(L))
    print("Menor dinheiro gasto em um item:", L[0])
    a = Dinheiro - soma
    if a < 1:
        print("Você está gastando demais")
        my_fucion()
    print("Seu saldo esse dia:", a)
    return(A, Dinheiro, Ja, L,C,i,soma,a)

#RETORNA UM DICIONARIO DE UM ARQUIVO JSON
def jsos(AF):
    with open(AF, 'r', encoding='utf8' ) as json_files: 
        data = json.load(json_files)
        return data

#ESCREVE EM UM ARQUIVO JSON USANDO UM DICIONARIO
def afe(data, AN):
    with open(AN, 'w', encoding='utf8' ) as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)     

def login():
    path = "./jsos.json"
    Cliente = jsos(path)
    while True:
        am = int(input("Você ja tem cadastro? se Sim digite 1 caso contrário digite 0: "))
        if am == 1:
            pae = input("Qual o Seu nome? ")
            if pae in Cliente.keys():
                kni = input("Qual A Sua senha? ")
                if Cliente[pae] == kni:
                    print("OBrigado; ")
                    break
                else:
                    print("tente novamente ")
            else:
                print("tente novamente ")
        elif am == 0:
            d = input("Qual o seu nome: ")
            Cliente[d] = input("Qual a senha? :")
            if len(Cliente[d]) > 3 and len(Cliente[d]) < 901:
                fi = input("Confime a senha: ") 
                if fi == Cliente[d]:
                    print(f"Sua senha é {Cliente[d]} e Seu Nome é {d}")
                    input("Pressione Enter para continuar: ")
                    afe(Cliente, path) 
            else:
                print("tente novamente")
                
        else: 
            am = int(input("Você ja tem cadastro? se Sim digite 1 caso contrário digite 0: "))    

#Programa funcionando e dando os resultados
login()
while True:
    amp = int(input("caso deseje fazer seu orçamento mensal digite 2, para anual 1, ou diario digite 0, caso deseja finalizar o programa digite -1: "))
    if amp == 1: 
        pao = din()       
        print("O Valor gasto mensalmente:", pao[6])           
    elif amp ==2:   
        pao1=din1()    
        print("O Valor gasto anualmente foi: ", pao1[6]) 
    elif amp ==0:
        pao2 = din2() ##Puxar o valor de dentro de DEF
        print("O valor gasto diariamente foi: " ,pao2[6])  ##imprimir o valor de return fora do DEF
    elif amp ==-1:
        break
    else:
        print("Tente novamente")
        gum
