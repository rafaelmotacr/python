# Quebrando um número 

'''from math import floor
n = float(input('> Digite um número em ponto flutuante:'))
print(f'> A parte inteira do número {n} é {floor(n)}')'''

# ceil arredonda para cima 

# floor arredonda para baixo 

# trunc corta somente a parte inteira de um número! funciona assim ó: math.trunc(num)

# A função int(num) também serve para pegar a parte inteira do número!

n =  float(input('> Digite um número em ponto flutuante: \033[32m'))
print(f'\033[m> O número digitado foi \033[32m{n}\033[m e sua parte inteira é \033[36m{int(n)}\033[m.')

# ^ solução ideal