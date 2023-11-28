# validando expressões matemáticas

c = 0
lista = []
e = str(input('> Digite uma expressão matemática:')).strip().lower().replace(' ', '')
print(e)
for i in range(0, len(e)):
    lista.append(e[i])
    if e[i] in '()':
        c += 1
print(lista)
if c > 0:
    if c % 2 != 0:
        print(f'> A expressão é inválida! O número de parênteses é impar!')
    elif c % 2 == 0:
        if lista.index(')') != len(lista) - 1:
            if lista[lista.index(')') + 1] not in '*/+-':
               print(f'> A expressão é inválida! Não há operação após o parêntese.')  
        elif lista[lista.index('(') - 1] not in '*/+-':
            print(f'> A expressão é inválida! Não há operação antes do parêntese')  
    else:
        print(f'> A expressão é válida!')
elif '0' in lista:
    if lista[lista.index('0') - 1] in '*/':
        print(f'> A expressão é inválida! (Multiplicação ou divisão por zero)') 
    elif lista[lista.index('0') + 1] in '*/':
        print(f'> A expressão é inválida! (Multiplicação ou divisão por zero)') 
print(f'> foram digitados {c} parenteses;')
