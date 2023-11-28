# Função que calcula a àrea

def área(largura, comprimento):
    print(f'> A área de um terreno {largura} x {comprimento} m é de {largura * comprimento:.2f} m².\n')


print('-' * 15)
print('> Controle de terrenos')
print('-' * 15)
área(float(input('> Digite a largura (m): ')), float(input('> Digite o comprimento (m): ')))
