# Procurando uma strinf dentro de outra

n = str(input('> Digite o seu nome completo: \033[32m')).strip()
s = 'Silva' in n.title()
if s==True:
    print('\033[m> Você \033[36mpossui\033[m Silva no seu nome!')
else:
    print('\033[m> Você \033[31mnão\033[m possui Silva no seu nome!')
    