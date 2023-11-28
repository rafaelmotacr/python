# Custo da viagem

km = float(input('> Digite a distância da sua viagem em KM: \033[36m'))    
if km <= 200:
    print(f'\033[m> O preço da viagem recebeu taxa de \033[31mR$ 0,50\033[m por KM, resultando num custo de \033[32mR$ {km * 0.50:.2f}\033[m.')  
else: 
    print(f'\033[m> O preço da viagem recebeu taxa de \033[36mR$ 0,45\033[m por KM, resultando num custo de \033[32mR$ {km * 0.45:.2f}\033[m.')

