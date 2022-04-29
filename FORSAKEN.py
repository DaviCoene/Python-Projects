import ast

while True:
    entrada = input('Entre com alguma coisa:')
    valor = ast.literal_eval(entrada)
    print(type(valor))