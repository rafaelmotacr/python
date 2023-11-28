# Aumentos múltiplos

s = float(input('> Digite o seu salário atual: \033[33m'))
if s <= 1.250:
    print(f'\033[m> O seu salário era \033[33mR$ {s}\033[m e recebeu um aumento de \033[32m15%\033[m, passando a ser \033[36mR$ {s + (s * 15 / 100)}\033[m.')
else:
    print(f'\033[m> O seu salário era \033[33mR$ {s}\033[m e recebeu um aumento de \033[35m10%\033[m, passando a ser \033[36mR$ {s + (s * 10 / 100)}\033[m.') 
