# Tabuada v2.0

l = int(input('> Digite um número e faremos a tabuada dele: \033[35m'))
print('\033[m-' * 14)
for i in range(1, 11):
    print(f'> \033[31m{l}\033[m x \033[34m{i:2^0}\033[m \033[32m=\033[m \033[35m{l * i}\033[m.')
print('\033[m-' * 14)
