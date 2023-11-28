# validando expressões matemáticas

lista = []
expr = str(input('> Digite sua expressão: '))
for i in expr:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('> A expressão digitada é \033[32mválida\033[m.\n')
else:
    print('> A expressão digitada é \033[31minváldia\033[m.\n')
    