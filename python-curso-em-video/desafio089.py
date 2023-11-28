# Boletim com notas compostas

etapa = total = 0
boletim = []
while True:
    if etapa == 0:
        print('-=-' * 15)
        nome = str(input(f'> Nome do {total}º aluno: \033[31m')).strip().title()
        nota1 = float(input(f'\033[m> Primeira nota de \033[31m{nome}\033[m: '))
        nota2 = float(input(f'\033[m> Segunda nota de \033[31m{nome}\033[m: '))
        média = (nota1 + nota2) / 2
        boletim.append([nome, [nota1,nota2], média])
        total += 1
        etapa += 1
    if etapa == 1:
        resposta = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        if resposta == 's':
            etapa = 0
            continue
        elif resposta == 'n':
            break
        else:
            continue
print('-=-' * 15)
print(f'| {"NO."} - {"Nome"}{"Média":>30} |')
print('-' * 45)
for total in range(0, len(boletim)):
    if boletim[total][2] < 5:
        print(f'| {total}   - {boletim[total][0]:.<28}\033[31m {boletim[total][2]:<5.1f}\033[m |')
    else:
        print(f'| {total}   - {boletim[total][0]:.<28}\033[36m {boletim[total][2]:<5.1f}\033[m |')
print('-' * 45)
while etapa != 999:
    etapa = int(input('> Deseja detalhar as notas de algum aluno? Digite 999 para sair: ')) 
    print(f'> As notas de \033[31m{boletim[etapa][0]}\033[m são {boletim[etapa][1]}.' if etapa <= len(boletim) else '> Aluno não encontrado! Tente novamnte:')
    print('-=-' * 15)
print('> Finalizando...\n> Volte sempre!')
