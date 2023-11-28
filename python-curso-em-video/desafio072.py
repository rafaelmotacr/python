# Número por extenso

r = 's'
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
    'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
    'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte') 
while r in 's':
    while True:
        card = int(input('\n> Digite um número ente zero e vinte: '))
        if 0 <= card <= 20:
            break
        print(f'\033[31;40m> Tente novamente.\033[m')
    print(f'> Você digitou o número \033[31;40m{ext[card]}\033[m.\n')
    r = str(input('> Deseja rodar o programa novamente? [S/N]: ')).strip().lower()[0]
print('\033[30;40m> Obrigado por utilizar nosso programa!\033[m')
