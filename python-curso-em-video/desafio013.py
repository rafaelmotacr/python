# Reajuste salarial 

s = float(input('> Digita ae o seu salário atual, mestre: \033[30m'))
print(f'\033[m> O seu salário antes era R$ \033[31m{s:.2f}\033[m.\n> Com \033[33m15% de aumento\033[m, passou a ser: R$ \033[32m{s + (s * 15 / 100):.2f}\033[m.')
