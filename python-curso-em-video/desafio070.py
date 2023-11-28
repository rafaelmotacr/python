# Estatisticas em produtos

print('\033[31;40m> Carrinho de compras online cheeeeeck!\033[m')
np = t = e = mb = abv1000 = 0
lista = list()
re = 1
while True:
    if e == 0:
        print(f'\n-----| Produto {re} |-----\n')
        e += 1
    if e == 1:
        n = str(input('> Digite o nome do produto: '))
        p = float(input('> Digite o valor do produto: '))
        t += p
        e += 1
        if p > 1000:
            abv1000 += 1
        if re == 1:
            mb = p
            lista.append(n)
        elif p < mb and re > 1:
            if np == 0:
                lista.append(n) 
                np += 1            
                mb = p
            else:
                lista.append(n)
                mb = p
        elif p == mb:
            lista.append(n)
    if e == 2:
        r = str (input('> Quer continuar? [S/N]: ')).strip().upper()[0]
        if r == 'N':
            break
        elif r == 'S':
            e = 0
            re += 1
            continue
        else:
            continue
l = len(lista) - 1
if l == 1:
    print(f'\n> Foram comprados {re} produtos.\n> O Total da compra foi R$ {t:.2f}.\n> Desses {re} produtos, {abv1000} custam mais que mil reais.\n> O produto mais barato foi {lista[1]}, que custa R$ {mb:.2f}.\n')
else:
    print(f'\n> Foram comprados {re} produtos.\n> O Total da compra foi R$ {t:.2f}.\n> Desses {re} produtos, {abv1000} custam mais que mil reais.\n> Os produtos mais baratos foram ', end  = '') 
    for i in range(1, l + 1):
        if i == l - 1 :
            print(f'{lista[i]} e ', end = '')
        elif i == l:
            print(f'{lista[i]}', end = '')
        else:
            print(f'{lista[i]}, ', end = '')
    print(f'. Todos eles custam R$ {mb:.2f}.\n ')
