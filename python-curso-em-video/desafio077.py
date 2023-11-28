# Contando vogais em uma tupla

tupla = ('Denzel', 'Shirazu', 'Fabiola', 'Kazura', 'Sheldon', 'Alice', 'Sagasta', 'Sofia', 'Minerva')
tupla = sorted(tupla)
for i in tupla:
    print(f'> Na palavra \033[32m"{i:^7}"\033[m temos as vogais:', end = '')
    for cont in i:
        if cont.lower() in 'aeiou':
            print(f' {cont} ', end = '')
    print('.')
