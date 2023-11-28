# Maior e menor da sequência

ma = me = 0
for i in range (1, 6):
    p = float(input(f'> Digite o peso da pessoa nº{i}: '))
    if i == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print(f'> O maior peso digitado foi {ma:.2f} KG e o menor foi {me:.2f} KG.') 
