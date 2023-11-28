# ìndice de massa corporal 

a = float(input('\033[m> Digite sua altura: \033[31m'))
p = float(input('\033[m> Digite seu peso: \033[31m'))
imc = p / a ** 2
if imc < 18.5:
    print(f'\033[m> O seu IMC é de \033[31m{imc:.1f}\033[m.|Abaixo peso|')
elif 18.5 <= imc < 25:
    print(f'\033[m> O seu IMC é de \033[32m{imc:.1f}\033[m.|Peso ideal|')
elif 25 <= imc < 30:
    print(f'\033[m> O seu IMC é de \033[33m{imc:.1f}\033[m.|Sobrepeso|')
elif 30 <= imc < 40:
    print(f'\033[m> O seu IMC é de \033[33m{imc:.1f}\033[m.|Obesidade|')
else:
    print(f'\033[m> O seu IMC é de \033[31m{imc:.1f}\033[m.|Obesidade mórbida|')