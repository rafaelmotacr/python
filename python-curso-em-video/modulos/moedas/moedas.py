def aumentar(ent, percen, cifra = False):
    saida = ent + (ent * percen / 100)
    return saida if not cifra else form(saida)


def diminuir(ent, percen , cifra= False):
    saida = ent - (ent * percen / 100)
    return saida if not cifra else form(saida)


def dobro(ent, cifra = False):
    saida = ent * 2
    return saida if not cifra else form(saida)


def metade(ent, cifra = False):
    saida = ent // 2
    return saida if not cifra else form(saida)


def form(ent, moeda = "R$"):
    return f'{moeda} {ent}'.replace('.',',')


def resumo(preço, aumento, redução):
    print('---' * 15)
    print(f'{"RESUMO DO VALOR":^45}')
    print('---' * 15)
    print(f'{"Preço analisado":.<35}{form(preço)}')
    print(f'{"Dobro do preço":.<35}{dobro(preço, True)}')
    print(f'{"Metade do preço":.<35}{metade(preço, True)}')
    print(f'{f"{aumento}% de aumento":.<35}{aumentar(preço, aumento, True)}')  
    print(f'{f"{redução}% de redução":.<35}{diminuir(preço, redução, True)}')  
    print('---' * 15, '\n')

