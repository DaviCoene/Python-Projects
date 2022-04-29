def primo(n):
    for val in range(2,n):
        if n % val ==0:
            return False
    return True

def revela():
    n=int(input('escolha até onde quer ver os primos: '))
    for val in range (2,n+1):
        if (primo(val)):
            print(val)
    
while True:
    revela()
