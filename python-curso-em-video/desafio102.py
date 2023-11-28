# Funções para fatorial

def fatorial(n, show = False):
    """
    > Calcula o fatorial de um número.
    :param n: recebe o número para calculo do fatorial.
    :param show: opcional, controla se o processo do calculo deve ser exbido ou nao.
    :return: retorna o fatorial do número n. 
    """
    f = 1
    for c in range (n, 0, - 1):
        f *= c
        if show:
            if c > 1:
                print(f'{c}', end = ' x ')
            else:
                print(f'{c}', end = ' = ')
    return f


print('-' * 20) 
f = fatorial(5, True)
print(f)
