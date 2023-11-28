# Aquele clássico da média

n1 = float(input('\033[m> Digite a nota 1: \033[30m'))
n2 = float(input('\033[m> digite a nota 2: \033[30m'))
if (n1 + n2) / 2 < 5:
    print(f'\033[m> A média foi \033[31m{(n1 + n2) / 2}\033[m. Portanto, o aluno foi \033[31mREPROVADO!\033[m')
elif (n1 + n2) /2 >= 5 and (n1 + n2) / 2 < 7:
    print(f'\033[m> A média foi \033[33m{(n1 + n2) / 2}\033[m. Portanto, o aluno fará \033[33mRECUPERAÇÃO!\033[m')
else:
    print(f'\033[m> A média foi \033[36m{(n1 + n2) / 2}\033[m. Portanto, o aluno foi \033[36mAPROVADO!\033[m')
