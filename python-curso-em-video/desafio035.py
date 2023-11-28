# Analisador de triângulos v.1.0

print('\033[30m-=-' * 9)
print('Analisador de triângulos.')
print('-=-' * 9)
l1 = float(input('\033[m> Digite o primeiro lado do triângulo: \033'))
l2 = float(input('> Digite o segundo lado do triângulo: '))
l3 = float(input('> Digite o terceiro lado do triângulo: '))
if l1 + l2 > l3:
    print(f'> \033[36mÉ possível\033[m formar um triângulo com essas medidas.')  
else:
    print(f'> \033[31mNão é possível\033[m formar um triângulo com esass medidas.')