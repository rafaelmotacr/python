# Cadastro de trabalhador em Python

from datetime import date as data
dados = dict ()
print('\033[m','-=-' * 34)
dados['nome'] = str(input('> Digite o seu nome: \033[36m'))
dados['idade'] = data.today().year - int(input('\033[m> Ano de nascimento: \033[36m'))
dados['ctps'] = int(input('\033[m> Carteira de trabalho: \033[36m'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('\033[m> Ano de contratação: \033[36m'))
    dados['salário'] = float(input('\033[m> Salário atual: \033[36m'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - data.today().year
print('\033[m','-=-' * 34)
print(dados)
for i, j in dados.items():
    print(f'\033[m> {i} tem valor \033[31m{j}\033[m.')
