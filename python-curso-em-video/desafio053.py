# Detector de palíndromo

f = str(input('> Digite uma frase para testarmos se é ou não um palindromo: ')).strip().lower().replace(' ','')
d = 0 
j = len(f) - 1
print('> O inverso da palavra é: ', end = '')
for i in range (0, len(f)):
    print(f'{f[j]}', end = '')
    if f[i] != f[j]:
        d = 1
    j -= 1
if d == 0:
    print('\n> É palindromo!')
else:
    print('\n> Não é palindromo!')

# A inversão também poderia ser feita usando fatiamento da seguinte maneira: inverso = frase[::-1], evitando o uso do for
