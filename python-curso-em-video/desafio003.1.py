n1 = int(input('> Valor 1: '))
n2 = int(input('> Valor 2: '))

print(f'\n> A soma é: \033[32m{n1 + n2}\033[m.')
print(f'> A multiplicação é: \033[34m{n1 * n2}\033[m.')
print(f'> A divisão em float é: \033[36m{n1 / n2:.2f}\033[m.')
print(f'> A divisão em int é: \033[35m{n1 // n2}\033[m.')
print(f'> O primeiro número elevado ao segundo é: \033[31m{n1 ** n2}\033[m.')
