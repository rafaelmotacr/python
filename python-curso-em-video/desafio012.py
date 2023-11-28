# Calculando descontos

p = float(input('> Digite o preço atual do produto: \033[30m'))
print(f'\033[m> O produto que antes custava \033[31m{p:.2f} R$\033[m, com \033[32m5%\033[m de \033[33mdesconto\033[m aplicado custa: \033[34m{p - (p * 5 / 100):.2f}\033[34m R$\033[m.')
