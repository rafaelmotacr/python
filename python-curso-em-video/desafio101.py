# Função para votação


def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if 18 <= idade <  70:
        return f'> Com {idade} anos o voto é \033[31;40mobrigatório\033[m.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'> Com {idade} anos o voto é \033[32;40mopcional\033[m.'
    else:
        return f'> Com {idade} anos o voto é \033[30;40mnegado\033[m.'


print('---' * 15)
p = voto(int(input('> Em que ano você nasceu?: ')))
print(f'{p}') 
print('---' * 15)
