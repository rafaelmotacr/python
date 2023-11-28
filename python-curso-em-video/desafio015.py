# Aluguel de carros

km = float(input('> Quantos kilometros foram percorridos com o carro?: \033[31m'))
d = float(input('\033[m> Por quantos dias o carro foi alugado?: \033[36m'))
print(f'\033[m> Considerando que foram rodados \033[31m{km}\033[m km e que o carro foi alugado por \033[36m{d:.0f}\033[m dias, o valor a ser pago é:R$ \033[32m{d * 60 + km * 0.15:.2f}\033[m.')
