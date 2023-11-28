# Analisador de textos

n = str(input('> Digite seu nome completo: \033[36m')).strip()
print(f'\033[m> Seu nome, com todas as letras minúsculas: \033[32m{n.lower()}\033[m.')
e = n.count(' ')
print(f'> Seu nome \033[36m"{n}"\033[m possui \033[31m{len(n) - e }\033[m letras ao todo.')
p = n.split()
print(f'> O seu primeiro nome, \033[30m"{p[0]}"\033[m, possui \033[33m{len(p[0])}\033[m letras.')

''' A útima parte pode ser feta usando o n.find' ', que nos dirá onde termina o primeiro nome. dai pode ser feito o fatiamento
Para fatiar uma string, usa-se a frase entre colchetes e dois pontos. Ex: c[0:5:10]
O comando acima iria exibir a string desde a letra 0 até a 5, pulando de dez em dez caractéres, mesmo que isso seja impossivel 

'''