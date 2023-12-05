from datetime import datetime

currentYear = datetime.now().year
defaultcode = f'{datetime.now().year}{datetime.now().month}'

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
        self._psdata = personDate()


    def setAge(self):
        self.age = currentYear - self.psdata.year
        printf(f"{self.name}'s age is {self.age}.", 'blue', 'underline')


    def setBirthday(self, birthday = personDate()):
        self.psdata = birthday


    def setCode(self, pos):
        self.code = defaultcode + f'{pos}'
        printf(f"{self.name}'s code is {self.code}.", 'blue', 'underline')    


    def setCpf(self, CPF):
        self.cpf = CPF


    def setGender(self, gender):
        self.gender = gender


    def setName(self,name):
        self.name = name


colors = {
    'NULL':        '\033[m',
    'gray':        '\033[30m',
    'red':         '\033[31m',
    'green':       '\033[32m',
    'yellow':      '\033[33m',
    'blue':        '\033[34m',
    'purple':      '\033[35m',
    'ligth-blue':  '\033[36m',
}


effects = {
    'NULL':        '\033[m',
    'bold':        '\033[1m',
    'test':        '\033[2m',
    'italic':      '\033[3m',
    'underline':   '\033[4m',
    'shine':       '\033[5m'
}


def createStudent(studentsList= []):
    tmp = student()
    tmp.setName(readName())
    tmp.setBirthday(readBirthday())
    tmp.setAge()
    tmp.setGender(readGender())
    tmp.setCpf(readCPF())
    tmp.setCode(len(studentsList) + 1)
    printf('student successfully registered!', 'yellow', 'bold')
    studentsList.append(tmp)


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
    return inputf('Your Choice: ')


def printStudents(studentsList = []):
    tittle('LISTING STUDENTS', '=', 'green')
    for index in range (0, len(studentsList)):
        printf(f'{index + 1} - Name: {studentsList[index].name}.')
        printf(f'CPF: {studentsList[index].cpf}.')
        printf(f'Code: {studentsList[index].code}.')
        printf(f'Gender: {studentsList[index].gender}.')
        printf(f'Age: {studentsList[index].age}.')
    tittle('LISTING STUDENTS', '=', line = True)


def readBirthday():
    birthDay = personDate()
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
    printf(f'The date {birthDay.toString()} was defined as the birthday.', 'blue', 'underline')
    return birthDay


def readCPF():
    CPF = inputf('CPF: ')
    if len(CPF) != 14:
        printf('Your CPF must have at exactly 13 digits!', 'red', 'underline')
        return readCPF()
    printf(f"'{CPF}' was defined as the CPF.",'blue', 'underline')
    return CPF


def readGender():
    gender = 'NULL'
    gender = inputf("Gender(F/M): ")[0].strip().upper()
    if gender not in 'FM':
        printf(f'INVALID GENDER ({gender})! TRY AGAIN!', 'red', 'underline')
        return readGender()
    printf(f"'{gender}' was defined as the gender.", 'blue', 'underline')
    return gender


def readName():
    name = 'NULL'
    name = inputf('Name: ').strip()
    if not name.replace(' ', '').isalpha():
        printf('INVALID NAME! TRY AGAIN!', 'red', 'underline')
        return readGender()
    elif len(name) < 5:
        printf('THE NAME MUST CONTAIN AT LEAST FIVE(5) LETTERS! TRY AGAIN!', 'red', 'underline')
        return readGender()
    name = name.title()
    printf(f"'{name}' Was defined as the name.", 'blue', 'underline')
    return name
        

def tittle(string, char, color = "NULL", line = False):
    
    if(not line):
        print(f'{char}' * (len(string) + 4))
        print(f'{colors[color]}  {string}  \033[m')
        print(f'{char}' * (len(string) + 4))
    else:
        print(f'{char}' * (len(string) + 4))
