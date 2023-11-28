# Dissecando uma variável  

algo = input('> Digite algo: ').strip()
# testa o tipo da variável
print('> A priore, essa variável é do tipo:',type(algo))
# testa se possui apenas números
if algo.isnumeric() == True:
    print('> A frase \033[34mpossui\033[m apenas números!')
else:
    print('> A frase \033[31mnão possui\033[m apenas números!')
# testa se tem letras e números
if algo.isalnum() == True:
    print('> A frase \033[34mpossui\033[m letras e números!')
else:
    print('> A frase \033[31mnão possui\033[m letras e números!')
# testa se tem apenas letras do alfabeto
if algo.isalpha() == True:
    print('> A frase \033[34mposui\033[m letras do alfabeto!')
else:
    print('> A frase \033[31mnão possui\033[m apenas letras do alfabeto!')
# testa se esta em caps lock
if algo.isupper() == True:
    print('> A frase \033[34mestá\033[m em caps lock!')
else:
    print('> A frase \033[31mnão está\033[m em caps lock!')
# testa se está em minúsculo
if algo.islower() == True:
    print('> A frase \033[34mé composta\033[m apenas por letras minúsculas!')
else:
    print('> A frase \033[31mnão é composta\033[m apenas por letras minúsculas!')
# testa se possui apenas espaços
if algo.isspace():
    print('> A frase \033[34mécomposta\033[m apenas por espaços!')
else:
    print('> A frase \033[31mnão é composta\033[m apenas por espaços!')
# testa se apenas algumaas letras são maiúsclas ou minúsculas
if algo.istitle() == True:
    print('> A frase \033[34mcomeça\033[m com letra maúscula!')
else:
    print('> A frase \033[31mnão começa\033[m com letra maúscula!')
