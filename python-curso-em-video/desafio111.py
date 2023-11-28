# Transformando módulos em pacotes

from modulos.moedas import moedas
from modulos.dados import dados

p = dados.leiadinheiro('> Digite o preço: R$ ')
moedas.resumo(p, 80, 50)
