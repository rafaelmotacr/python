# Um print especial

def escreva(frase):
    print('-' * (len(frase) + 4))
    print(f'  {frase}')
    print('-' * (len(frase) + 4))


while True:
    escreva(str(input('> Digite uma frase (sair interrompe): ')))
