# Soma impares multiplos de três

c = s = 0
for p in range (1, 501, 2):
    if p % 3 == 0:
        s += p
        c += 1
print(f'> A soma de todos os {c} números impares e múltiplos de três entre 1 e 500  é igual a {s}.')
