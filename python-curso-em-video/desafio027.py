# Primeiro e último nome de uma pessoa 

n =  str(input('> Digite o seu nome completo: \033[30m')).strip()
n = n.split()
print(f'\033[m> Primeiro nome: \033[34m{n[0]}\033[m.')
print(f'> Último nome: \033[32m{n[len(n) - 1]}\033[m.')
