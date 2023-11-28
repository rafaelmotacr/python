# Valores únicos em uma lista

e = 0
lista = []
print('\033[m','-=-' * 10)
while True:
	if e == 0:
		n = int(input('\033[m> Digite um valor: \033[36m'))
		if n in lista:
			print('\033[m> Este número já existe na lista! Não será adcionado!')
		else:
			print('\033[m> Valor adicionado com suceso!') 
			lista.append(n)
		e += 1
	if e == 1:
		r = str(input('\033[m> Deseja continuar? [S/N]: \033[36m')).strip().lower()[0]
		if r == 'n':
			break
		elif r == 's':
			print('\033[m','-=-' * 10)
			e = 0
			continue
		else:
			continue
print('\033[m','-=-' * 10)
lista.sort()
print(f'\033[m> Você digitou os valores \033[32m{lista}.\033[m\n ')


		