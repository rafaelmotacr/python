# Analisador de triângulos v.1.0

print('\033[30m-=-' * 9)
print('Analisador de triângulos.')
print('-=-' * 9)
l1 = float(input('\033[m> Digite o primeiro lado do triângulo: \033[32m'))
l2 = float(input('\033[m> Digite o segundo lado do triângulo : \033[32m'))
l3 = float(input('\033[m> Digite o terceiro lado do triângulo: \033[32m'))
if l3 < l1 + l2 and l2 < l1 + l3 and l1 < l2 + l3:
    print(f'\033[m> \033[36mÉ possível\033[m formar um triângulo com essas medidas.') 
    if l1 == l2 == l3:
        print('> Este é um triângulo equilátero!')
    elif l1 == l2 or l2 == l3 or l1 == l3 or l1: 
        print('> Este é um triângulo isócelis!')
    else:
        print('> Este é um triângulo escaleno!')
else:
    print(f'\033[m> \033[31mNão é possível\033[m formar um triângulo com esass medidas.')  
 