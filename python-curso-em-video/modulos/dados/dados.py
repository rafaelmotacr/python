def leiadinheiro(msg = ''):
    while True:
        ent = str(input(msg)).replace(',', '.').strip()
        if ent.isalpha() or ent == '':
            print(f'\033[31mERRO: \'{ent}\' não é um valor inválido!\033[m')
        else:
            return float(ent)

