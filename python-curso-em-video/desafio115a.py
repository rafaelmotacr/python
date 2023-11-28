#  Criando um menu

from modulos.desafio115 import desafio115
from time import sleep 

arq = 'cursoemvideo.txt'

if not desafio115.arquivo_existe(arq):
    desafio115.criar_arquivo(arq)

while True: 
    resposta = desafio115.menu(['Ver pessaos cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        desafio115.cabeçalho('opção 1')
    elif resposta == 2:
        desafio115.cabeçalho('opção 2')
        desafio115.leia_arquivo(arq)
    elif resposta == 3:
        desafio115.cabeçalho('\'programa\' está deixando o chat...')
    else:
        desafio115.cabeçalho('Opção inválida!')
    sleep(1)
