# Exercitando módulos em Python

from modulos.moedas import moedas

p = float(input('> Digite o preço: R$ '))
print(f'> A metade de {moedas.form(p)} é {moedas.metade(p, True)}.')
print(f'> O dobro de {moedas.form(p)} é {moedas.dobro(p, True)}.')
print(f'> Aumentando 10%, temos {moedas.aumentar(p, 10, True)}.')
print(f'> Diminuindo 13%, temos {moedas.diminuir(p, 13, True)}.\n')
