# Unindo dicionários em listas

etapa = média = 0 
pessoa = list()
cadastro = dict()
mulher = list ()
print('-=-' * 15)
while True:
    cadastro.clear()
    if etapa == 0:
        cadastro['nome'] = str(input('> Nome: '))
        etapa += 1  
    if etapa == 1:
        cadastro['sexo'] = str(input('> Sexo: ')).upper()[0]
        if cadastro['sexo'] in 'MF':
            if cadastro['sexo'] == 'F':
                mulher.append(cadastro['nome'][:])
            etapa += 1
            continue
        print('> Erro! Responda apenas com M ou F!') 
    if etapa == 2: 
        cadastro['idade'] = int(input('> Idade: '))
        média += cadastro['idade']
        etapa += 1
    if etapa == 3:
        resposta = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        if resposta == 's':
            etapa = 0
            pessoa.append(cadastro.copy())
            print('-=-' * 15)
            continue
        elif resposta =='n':
            pessoa.append(cadastro.copy())
            média /= len(pessoa)
            print('-=-' * 15)
            break
        print('> Erro! Responda apenas com s ou n!')
print(f'> Ao todo, foram cadastradas {len(pessoa)} pessoas.')
print(f'> A média de idade do grupo é de: {média:5.2f} anos.')
print(f'> As mulheres cadastradas foram: ', end = '')
for i in range(0, len(mulher)):
    if i == len(mulher) - 1:
        print(f'{mulher[i]}', end = '.\n')
    elif i == len(mulher) - 2:
        print(f'{mulher[i]}', end =' e ')
    else:
        print(f'{mulher[i]}', end = ', ')
print('> lista das pessoas acima da média de idade:\n ')
for j in pessoa:
    if j['idade'] >= média:
        for k, l in j.items():
            print(f'{k} = {l}', end = '; ')
        print()
print('\n<<<< Encerrado >>>>\n')       
