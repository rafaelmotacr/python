# Catetos e hipotenusa

co = float(input('> Digite o comprimento do cateto oposto do triângulo: \033[31m'))
ca = float(input('\033[m> Digite o comprimento do cateto adjascente do triângulo: \033[36m'))

# o quadrado da hipoternusa é igual a soma dos quadrados dos catetos. Ou seja, a raiz quadrada da soma dos catetos é a hipotenusa
# elevar a um meio (1/2) equivale a fazer a raiz quadrada de um número, assim como elevar a um terçp (1/3) equivale à raiz cúbica

hip = (ca ** 2 + co ** 2) ** (1 / 2)

#ou

'''from math import hypot
hypot(co,ca)'''

print(f'\033[m>\033[33m O valor da hipoternusa é: \033[32m{hip:.2f}\033[m.')
