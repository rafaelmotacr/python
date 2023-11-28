# Verificando as primeiras letras de um texto

c = str(input('> Digite o nome da sua cidade: \033[30m')).strip().lower()
c = c.split()
s = 'santo' in c[0]
if(s==True):
    print('\033[m> O nome da sua cidade \033[36mcomeça\033[m com Santo!')
else:
    print('\033[m> O nome da sua cidade \033[31mnão\033[m começa com Santo!')
'''Alternativamente, eu poderia ter usado um recorte que deveria analidar somente as cinco primeiras 
letras, as quais deveriam formar a palavra 'santo'. Faria isso atrávez da comparação entre c[:5]=='santo'.
isso retornaria um valor falso ou verdadeiro, dentro de um print'''     
