# Média aritimética

n = str(input('> Digite o nome do aluno: ')).strip()

n1 = float(input(f'> Digite a primeira nota de \033[36m{n}\033[m: '))
n2 = float(input(f'> Digite a segunda nota de \033[36m{n}\033[m: '))
if (n1 + n2) / 2 >= 5:
    print(f'> A média de \033[36m{n}\033[m é: \033[34m{(n1 + n2) / 2 :.1f}\033[m.')
else:
    print(f'> A média de \033[36m{n}\033[m é: \033[31m{(n1 + n2) / 2 :.1f}\033[m. Ele precisa estudar mais!')