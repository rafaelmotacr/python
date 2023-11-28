# primeira e última ocorrência de uma string

f = str(input('> Digite uma frase qualquer: \033[36m')).lower().strip()
a = f.count('a')
p = f.find('a')
l = len(f)
# Comçea a contar a partir da direita, ou seja, do fim.
u = f.rfind('a')
print(f'\033[m> A letra a aparece \033[33m{a}\033[m vezes.')
print(f'> A letra a aparece pela primeira vez na posição \033[33m{p + 1}\033[m.')
print(f'> A letra a aparece pela última vez na posição \033[33m{u + 1}\033[m.\n')
