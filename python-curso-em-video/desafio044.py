# Gerenciador de pagamentos

print('-=-' * 5,'lojinha do Mitinho','-=-' * 5)
p = float(input('> Qual o valor total das compras?: \033[30;40m'))
print(f'''\033[m> Você pode pagar das seguintes formas:

[1] - À vista no dinheiro ou cheque \033[32m(Poggers)\033[m
[2] - À vista no cartão \033[32m(Poggers)\033[m
[3] - 2x no cartão \033[31m(Noggers)\033[m
[4] - 3x ou \033[32mmais\033[m no cartão \033[31m(Noggers)\033[m''')
i = int(input('\n> Digite sua escolha: \033[30;40m'))
if i == 1:
    print(f'\033[m> Pagando à vista no dinheiro ou cheque, sua compra de R$ {p:.2f} recebeu um desconto de 10%, passando a custar R$ {p - (p * 10 / 100)}. ')
elif i == 2:
    print(f'\033[m> Pagando à vista no cartão, sua compra de R$ {p:.2f} recebeu um desconto de 5%, passando a custar R$ {p - (p * 5 / 100)}. ')
elif i == 3:
    print(f'\033[m> Pagando em 2x no cartão, sua compra irá custar R$ {p:.2f}.')
elif i == 4:
    d = int(input('> Digite em quantas vezes pretente parcelar: \033[30;40m'))
    print(f'\033[m> Pagando em {d}x no cartão, sua compra que custava R$ {p:.2f} terá parcelas de R$ {(p + (p * 20 / 100)) / d:.2f} e recebeu um juros de 20%, custando agora R$ {p  + (p * 20 /100):.2f} ao todo. ')
else:
    print(f'\033[m> A opção digitada é inválida!')
