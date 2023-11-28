# Analisador completo

n = me = cf = cm = 0
for i in range (1, 5):
    print(f'\033[32m-------- {i}º Pessoa ---------\033[m')
    nome = str(input(f'> Nome da {i}º pessoa: ')).strip()
    idade = int(input(f'> Idade da {i}º pessoa: '))
    sexo = int(input(f'> Sexo da {i}º pessoa:\n\n[1] - Homem\n[2] - Mulher\n\n> Sua escolha: '))
    me += idade
    if sexo == 2 and idade < 20:
        cf += 1
    elif sexo == 1 and idade > cm:
        n = '' + nome
        cm = idade
me /= 4
print(f'\n\033[32m---------Resultado---------\033[m\n')
if cf > 1:
    print(f'> A média de idade do grupo é de {me} anos.\n> O homem mais velho do grupo se chama {n} e tem {cm} anos.\n> Existem {cf} mulheres com menos de 20 anos no grupo.')
else:
     print(f'> A média de idade do grupo é de {me} anos.\n> O homem mais velho do grupo se chama {n} e tem {cm} anos.\n> Existe uma mulher com menos de 20 anos no grupo.')
