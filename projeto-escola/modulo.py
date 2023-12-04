from datetime import datetime

class personDate:
    def __init__(self,day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    def toString(self):
        return f'({self.day:0>2}/{self.month:0>2}/{self.year})'


class student:
    def __init__(self,name = "No name", age = 0, code = "NULL", CPF = "NULL", gender = "NULL", psdata = personDate()):
        self._name = name
        self._age = age
        self._code = code
        self._cpf = CPF
        self._gender = gender


    def setName(self,name):
        self.name = name
    

    def setAge(self,age):
        self.age = age


    def setCode(self, code):
        self.code = code


    def setCpf(self, CPF):
        self.cpf = CPF

    
    def setGender(self, gender):
        self.gender = gender


colors = {
    'NULL':'\033[m',
    'gray':'\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'ligth-blue': '\033[36m',
}


effects = {
    'NULL':'\033[m',
    'bold':'\033[1m',
    'test':'\033[2m',
    'italic':'\033[3m',
    'underline':'\033[4m',
    'shine':'\033[5m'
}


def printf(string = "NULL", color = "NULL", effect = "NULL"):
    print(f'> {effects[effect]}{colors[color]}{string}\033[m')


def readInt(string = 'NULL', color = 'green',):
    tmp = input(f'> {string}{colors[color]}')
    print('\033[m', end='')
    try:
        tmp = int(tmp)
    except ValueError:
        printf('This entry must be a integer!', 'red', 'underline')
        return readInt(string, color)
    else:
        return tmp


def inputf(string = 'NULL', color = 'green', mode = 'str'):
    if mode == 'str':  
        tmp = input(f'> {string}{colors[color]}')
    elif mode == 'int':
        tmp = readInt(string, color)
    print('\033[m', end = '')
    return tmp


def mainMenu():
    tittle("MAIN MENU", '=', 'yellow')
    print('[0] - QUIT')
    print('[1] - CREATE STUDENT')
    print('[2] - REMOVE STUDENT')
    print('[3] - UPDATE STUDENT')
    print('[4] - VIEW STUDENTS')
    tittle('MAIN MENU', '=', line = True)


def readAge():
    birthDay = personDate()
    currentYear = datetime.now().year
    day = month = year = 0

    while True:
        day = inputf('Day: ', mode = 'int')
        if not(32 > day and  day > 0):
            printf('Ivalid day!', 'red', 'underline')
            continue
        break

    while True:
        month = inputf('Month: ', mode = 'int')
        if not(13 > month and  month > 0):
            printf('Ivalid Month!', 'red', 'underline')
            continue
        break

    while True:
        year = inputf('Year: ', mode = 'int')
        if not(currentYear > year and  year > 0 and 1980 < year):
            printf('Ivalid Year!', 'red', 'underline')
            continue
        break

    birthDay.day = day
    birthDay.month = month
    birthDay.year = year
    printf(f'the date {birthDay.toString()} was defined as the birthday.', 'blue', 'underline')
    return birthDay


def readCPF():
    CPF = inputf('CPF: ')
    if len(CPF) != 14:
        printf('Your CPF must have at exactly 13 digits!', 'red', 'underline')
        return readCPF()
    return CPF


def readGender():
    gender = 'NULL'
    while gender not in 'FM':
        gender = inputf("> Gender(F/M): ")[0].strip().upper()
        if gender not in 'FM':
            printf(f'INVALID GENDER ({gender})! TRY AGAIN!', 'red', 'underline')
    printf(f'{gender} was defined as the gender.', 'blue', 'underline')
    return gender


def readName():
    name = 'NULL'
    while True:
        name = inputf('> Name: ').strip()
        if not name.replace(' ', '').isalpha():
            printf('INVALID NAME! TRY AGAIN!', 'red', 'underline')
            continue
        elif len(name) < 5:
            printf('THE NAME MUST CONTAIN AT LEAST FIVE(5) LETTERS! TRY AGAIN!', 'red', 'underline')
            continue
        name = name.title()
        printf(f'{name} Was defined as the name.', 'blue', 'underline')
        break
    return name
        

def tittle(string, char, color = "NULL", line = False):
    
    if(not line):
        print(f'{char}' * (len(string) + 4))
        print(f'{colors[color]}  {string}  \033[m')
        print(f'{char}' * (len(string) + 4))
    else:
        print(f'{char}' * (len(string) + 4))


