# Radar eletrônico

v = float(input('> Digite imediatamente a velocidade do seu carro: \033[36m'))
if v > 80:
    print(f'\033[m> Você foi \033[33mmultado\033[m por andar \033[31macima\033[m do limite de velocidade permitido \033[32m(80 KM/H)\033[m!\n\033[m> A multa irá custar R$ \033[31m{(v - 80) * 7:.2f}\033[m.')
else:
    print(f'> \033[35m> Dessa vez, você se salvou, safadinho!\033[m\n')
