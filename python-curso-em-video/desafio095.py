# Cadastro de um jogador de futebol

etapa = 0
gol = list ()
cadastro = dict ()
jogadores = list()
print('-=-' * 18)
while True:
    if etapa == 0:
        cadastro['nome'] = str(input('> Digite o nome do jogador: '))
        l = int(input(f'> Quantas partidas {cadastro["nome"]} jogou?: '))
        for i in range(0, l):
            gol.append(int(input(f'> Quantos gols na partida {i + 1}?: ')))
        cadastro['gols'] = gol[:]
        cadastro['total'] = 0
        for i in range (0, l):
            cadastro['total'] += gol[i]
        etapa += 1
    if etapa == 1:
        resposta = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        if resposta == 's':
            etapa = 0
            jogadores.append(cadastro.copy())
            gol.clear()
            print('-=-' * 18)
            continue
        elif resposta == 'n':
            jogadores.append(cadastro.copy())
            etapa += 1
            gol.clear()
            continue
        print('Resposta inválida! Tente novamente!')
    if etapa == 2:
        print('-=-' * 18 )
        print(f'{"Cod":>3} {"Nome":<15}{"Gols":<20}{"total":>10}')
        print('---' * 18 )
        for i in jogadores:
            print(f'{jogadores.index(i):<3} {i["nome"]:<15}{str(i["gols"][:]):<20}{i["total"]:>10}')
        print('---' * 18 )
        etapa += 1
    if etapa == 3:
        l = int(input('> Mostrar dados de qual jogador?: '))
        if l <= len(jogadores):
            print(f'\n===== Levantamento do jogador {jogadores[l]["nome"]} =====\n')
            for i in range (0, len(jogadores[l]["gols"])):
                print(f'No jogo {i} ele fez {jogadores[l]["gols"][i]} gols.')
            print('---' * 18)
        elif l == 999:
            print('Encerrando...')
            break
        else: 
            print(f'> Erro! Não existe jogador com código {l}!')
