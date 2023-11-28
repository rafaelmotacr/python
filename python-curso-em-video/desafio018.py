# Seno, cosseno e tangente

from math import sin,cos,tan,radians
a = float(input(f'> Digite o ângulo do circulo trigonométrico: \033[35m'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

# As funções de seno, cosseno e tangente em pythons trazem dados em graus radianos, então iremos converter para centigrados

print(f'\033[m> O seno é: \033[31m{s:.2f}\033[m.\n> O cosseno é: \033[32m{c:.2f}\033[m.\n> A tangente é: \033[33m{t:.2f}\033[m.')
