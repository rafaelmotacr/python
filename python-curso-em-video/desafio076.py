# Lista de preços com tuplas

loja = ('Caneta', 2.45, 'Lápis', 1.23,'Lapizeira', 0.50, 'Hidrocor', 10, 'Grafite', 3.75,  'Borrachar', 56, 'Mochila', 60, 'Estojo', 15, 'caderno', 17, 'Sapato', 90, 'Celularesrgftsrtsreser', 60)
print( '-' * 50)
print('| {}{:^46}{} |'.format('\033[34;40m','listagem de Preços','\033[m'))
print( '-' * 50)
print('| {:>8}{:^30}{:<8} |'. format('Produto', '|', 'Preço'))
print( '-' * 50)
cont = 1
for i in range (0, len(loja), 2):
    print(f'| {cont:2} - {loja[i]:.<32} R$ {loja[i + 1]:>5.2f} |')
    cont += 1
print( '-' * 50)
