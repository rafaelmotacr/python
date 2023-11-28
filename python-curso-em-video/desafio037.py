# Conversor de bases númericas

n = int(input('\033[m> Digite um número: \033[36m'))
b = int(input('''\033[m> Para qual base deseja que o número seja convertido?
> 1 - Binário
  2 - Octal
  3 - Hexadecimal
> Sua resposta: \033[m'''))
if b == 1:
    print(f'> O número \033[36m{n}\033[m na base binária é: \033[32m{(bin(n))[2:]}\033[m.')
elif b == 2:
    print(f'> O número \033[36m{n}\033[m na base octal é: \033[33m{oct(n)[2:]}\033[m.')
elif b == 3:
    print(f'> O número \033[36m{n}\033[m na base hexadecimal é: \033[35m{hex(n)[2:]}\033[m.')
else:
    print('> A resposta digitada é inválida!')
