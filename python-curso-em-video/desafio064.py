# Tratando vários valores v1.0

print('\033[31;40m> Bem vindo ao.. Somador de números?\n')
n = c = s = 0
while n != 999:
    s += n
    c += 1
    n = int(input('\033[31;40m> Digite um \033[32;40mnúmero\033[31;40m diferente de 999:\033[0;0;33m ')) 
print(f'\033[31;40m> Foram digitados {c} \033[32;40mnúmeros\033[31;40m e a soma de todos eles vale {s}.\033[m')
