# Lista composta e análise de dados

abaixo = []
acima = []
entrada = []
lista = []
maior = menor = e = np = 0
while True: 
    if e == 0:
        entrada.append(str(input('> Digite o nome: ')))
        entrada.append(float(input('> Digita o peso: ')))
        lista.append(entrada[:])
        entrada.clear()
        e += 1
    if e == 1:
        resposta = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        print('-=' * 15)
        if resposta == 'n':  
            break
        elif resposta == 's':
            e = 0
            continue
        else:
            continue
for i in range (0, len(lista)):
    if i == 0:
        maior = lista[i][1]
        menor = lista[i][1] 
    elif lista[i][1] > maior:
        maior = lista[i][1]
    elif lista[i][1] < menor:
        menor = lista[i][1]
for pessoa in lista:
    if menor in pessoa:
        abaixo.append(pessoa[0])
    elif maior in pessoa:
        acima.append(pessoa[0])
print(f'> Foram cadastradas {len(lista)} pessoas. O maior peso foi {maior:.2f}, sendo o peso de {acima}. O menor peso foi {menor:.2f}, sendo o peso de {abaixo}.')
    