# Validação de dados

r =  str(input('> Digite o seu sexo [F/M]: ')).strip().upper()[0]
while r not in 'fFmM':
    r =  str(input('> Dados inválidos! Digite o seu sexo corretamente: [F/M]: ')).strip().upper()[0]
if r in 'fF':
    print('> Entendo, você é uma mulher!')
elif r in 'mM':
    print('> Entendo, você é um homem!')
else: 
    print('> Sexo inválido!') 