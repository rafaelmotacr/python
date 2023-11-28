mi = ('', 'Mil', 'Dois mil', 'Três mil', 'Quatro mil', 'Cinco mil', 'Seis mil', 'Sete mil', 'Oito Mil', 'Nove mil')
ce = ('Cem', 'Cento', 'Duzentos', 'Trezentos','Quatrocentos', 'Quinhentos', 'Seicentos', 'Setecentos', 'Oitocentos', 'Novecentos')
de = ('', 'Dez', 'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa')
du = ('', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove')
un = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove') 

n = 0
while True:

    n = int(input('\n> Digite o número que deseja escrever por extenso: '))

    m = n // 1000
    c = n // 100 % 10
    d = n // 10 % 10
    u = n % 10

    print(f'> O número é: \033[31;40m', end = '')
    if m > 0:
        print(f'{mi[m]}', end = ' ')
        print('e ' if c > 0 and d == 0 and u == 0 else '', end = '') 
    if c > 0:
        if c == 1 and d == 0 and u == 0:
            print(f'{ce[c - 1]}', end ='')
        elif (d > 0 or u > 0):  
            print(f'{ce[c]}', end = ' ')
            print('e ', end = '')
        else: 
            print(f'{ce[c]}', end = ' ')
    if (m != 0 and c == 0) and (d != 0 or u != 0):
        print ('e ', end ='') 
    if d > 0:
        if d == 1 and u > 0:
            print(f'{du[u]}', end = '')
        elif d > 1 and u > 0:
            print(f'{de[d]}', end = ' ')
            print('e ', end = '')
        else: 
            print(f'{de[d]}', end = '')
    if u >= 0 and d != 1:
        if u == 0 and d == 0 and c == 0 and m == 0:
            print('Zero', end = '')
        elif  u == 0:
            print('', end = '')
        else:
            print(f'{un[u]}', end = '')
    print('.\033[m')
