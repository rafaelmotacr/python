# Grupo da maioridade

from datetime import date
a = date.today().year
ma = me = 0
for i in range (1, 8):
    n = a - int(input(f'> Digite o ano de nascimento da pessoa nº {i}: '))
    if n >= 21:
        ma += 1
    else:
        me += 1
print(f'> Dentre as pesoas mencionadas, {ma} já atingiram a maioridade e {me} ainda não atingiram.')
