# Conversor de medidas

n = float(input('\033[33m> Digite um valor em metros: '))
print(f'\033[m \n> Em Kilometros:\033[31m{n / 1000 : 10.3f}\033[m KM.')
print(f'> Em Hecctômetro:\033[31m{n / 100 :8.2f}\033[m HM.')
print(f'> Em Decâmetro:\033[31m{n / 10 : 9.1f}\033[m DAM.')
print(f'> Em Metros:\033[32m{n:10.0f}\033[m M.')
print(f'> Em Decimetros:\033[34m{n * 10 : 7.0f}\033[m DM.')
print(f'> Em Centimetros:\033[34m{n * 100 : 7.0f}\033[m CM.')
print(f'> Em Milimetros:\033[34m{n * 1000 : 9.0f}\033[m MM.\n')
