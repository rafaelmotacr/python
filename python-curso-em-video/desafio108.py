# formatando moedas em python

from modulos.moedas import moedas

p = float(input('> Digite o preço: R$ '))
print(f'> A metade de {moedas.form(p)} é {moedas.form(moedas.metade(p))}.')
print(f'> O dobro de {moedas.form(p)} é {moedas.form(moedas.dobro(p))}.')
print(f'> Aumentando 10%, temos {moedas.form(moedas.aumentar(p, 10))}.')
print(f'> Diminuindo 13%, temos {moedas.form(moedas.diminuir(p, 13))}.\n')
