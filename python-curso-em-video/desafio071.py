# Simulador de caixa eletrônico

cedula = 50
uso = 0
print('\033[31;40m> Banco do balacobaco!\033[m\n')
v = int(input('> Digite o valor a ser sacado: R$ '))
while True:
    if v >= cedula:
        v -= cedula
        uso += 1
    else:
        if uso >= 1:
            print(f'> Foram usadas {uso} cédulas de {cedula} reais.')
        uso = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if v == 0:
           break
print('\n\033[31;40m> Viadagem!\033[m\n')

            