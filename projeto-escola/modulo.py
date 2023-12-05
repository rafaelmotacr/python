from datetime import datetime

currentYear = datetime.now().year
defaultCode = str ()
if(datetime.now().month < 7):
   defaultCode = f'{datetime.now().year}001'
else:
    defaultCode = f'{datetime.now().year}002'

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


class personDate:
    def __init__(self,day = 0, month = 0, year = 0):
        self._day = day
        self._month = month
        self._year = year


    def setDay(self, day):
        self.day = day

    
    def setMonth(self, month):
        self.month = month


    def setYear(self, year):
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
        self.code = defaultCode + f'{pos}'
        printf(f"{self.name}'s code is {self.code}.", 'blue', 'underline')    


    def setCpf(self, CPF):
        self.cpf = CPF


    def setGender(self, gender):
        self.gender = gender


    def setName(self,name):
        self.name = name


    def getAge(self):
        return self.age 
    

    def getCode(self):
       return self.code 
    

    def getCpf(self):
        return self.cpf
    

    def getGender(self):
        return self.gender
    

    def getName(self):
        return self.name


# Crud functions

def createStudent(studentsList = []):
    tittle('CREATE STUDENT','=', 'green')
    tmp = student()
    tmp.setName(readName())
    tmp.setBirthday(readBirthday())
    tmp.setAge()
    tmp.setGender(readGender())
    tmp.setCpf(readCPF())
    tmp.setCode(len(studentsList) + 1)
    printf('Student successfully registered!', 'yellow', 'bold')
    studentsList.append(tmp)


def printPerson(num = int(), person = student(), isTheOnly = False):
    if isTheOnly:
        printf(f'Name: {person.name}.')
    else:
        printf(f'{num + 1} - Name: {person.getName()}.')
    printf(f'CPF: {person.getCpf()}.')
    printf(f'Code: {person.getCode()}.')
    printf(f'Gender: {person.getGender()}.')
    printf(f'Age: {person.getAge()}.')




def removeStudent(studentsList = []):

    choice = code = 0
    target = student()
    
    if len(studentsList) == 0:
        printf("There aren't students to remove. Come back later...", 'red', 'underline')
        return

    tittle('REMOVE MENU','=', 'red')
    print('[0] - BACK')
    print('[1] - REMOVE USING CODE')
    print('[2] - VIEW STUDENTS AND REMOVE')
    tittle('REMOVE MENU','=', 'red', True)
    choice = inputf('Your choice: ', mode= 'str')

    if choice == '0':
        return
    elif choice == '1':

        code = inputf('Enter the student code: ')

        if validateStudent(code, studentsList):

            target = searchStudent(code, studentsList)
            printf('Student suceffuly removed.', 'blue', 'underline')
            studentsList.remove(target)

        else:

            printf('Invalid student! Try again!', 'red', 'underline')
            return removeStudent(studentsList)

    elif choice == '2':

        printList(studentsList)
        code = inputf('Your choice: ', mode ='int')

        if(code > len(studentsList) or code <= 0):

            printf('Invalid student! Try again!', 'red', 'underline')
            return removeStudent(studentsList)
        
        else:

            printf('Student suceffuly removed.', 'blue', 'underline')
            studentsList.pop(code - 1)

    else:
        printf('Invalid choice! Try again!', 'red', 'underline')


def updateCentral(studentsList = []):
    
    if len(studentsList) == 0:
        printf("There aren't students to update. Come back later...", 'red', 'underline')
        return

    choice = code = 0
    target = student()

    tittle('UPDATE MENU','=', 'purple')
    print('[0] - BACK')
    print('[1] - UPDATE USING CODE')
    print('[2] - VIEW STUDENTS AND UPDATE')
    tittle('UPDATE MENU','=', 'purple', True)

    choice = inputf('Your choice: ', mode= 'str')

    if choice == '0':
        return
    elif choice == '1':

        code = inputf('Enter the student code: ')

        if validateStudent(code, studentsList):

            target = searchStudent(code, studentsList)
            updateStudent(target)

        else:

            printf('Invalid student! Try again!', 'red', 'underline')
            return updateCentral(studentsList)
            
    elif choice == '2':

        printList(studentsList)
        code = inputf('Your choice: ', mode ='int')

        if(code > len(studentsList) or code <= 0):

            printf('Invalid student! Try again!', 'red', 'underline')
            return updateCentral(studentsList)
        
        else:

            updateStudent(studentsList[code -1])

    else:
        printf('Invalid choice! Try again!', 'red', 'underline')


def updateStudent(person = student()):
    quit = False
    while not quit:
        choice = updateMenu(f'{person.getName()}')
        tittle('> your choice', '=', line = True)
        if choice == '0':
            quit = True
            continue
        elif choice == '1':
            printPerson(0, person, True)
        elif choice == '2':
            person.setBirthday(readBirthday())
            person.setAge()
        elif choice == '3':
            person.setCpf(readCPF())
        elif choice == '4':
            person.setGender(readGender())
        elif choice == '5':
            person.setName(readName())
        else:
            printf('Invalid choice! Try again!', 'red', 'underline')
            updateStudent(person)

# Menu / UI functions

def mainMenu():
    tittle("MAIN MENU", '=', 'yellow')
    print('[0] - EXIT')
    print('[1] - CREATE STUDENT')
    print('[2] - REMOVE STUDENT')
    print('[3] - UPDATE STUDENT')
    print('[4] - VIEW STUDENTS')
    tittle('MAIN MENU', '=', line = True)
    return inputf('Your Choice: ')


def updateMenu(string = str()):
    tittle(f'{string.upper()}', '=', 'purple')
    print('[0] - BACK')
    print('[1] - SEE DATA')
    print('[2] - UPDATE BIRTHDAY')
    print('[3] - UPDATE CPF')
    print('[4] - UPDATE GENDER')
    print('[5] - UPDATE NAME')
    tittle(f'{string.upper()}', '=', 'purple', True)
    return inputf('Your Choice: ')


def tittle(string, char, color = "NULL", line = False):
    
    if(not line):
        print(f'{char}' * (len(string) + 4))
        print(f'{colors[color]}  {string}  \033[m')
        print(f'{char}' * (len(string) + 4))
    else:
        print(f'{char}' * (len(string) + 4))


# Personalized Input / output functions

def inputf(string = 'NULL', color = 'green', mode = 'str'):
    if mode == 'str':  
        tmp = input(f'> {string}{colors[color]}')
    elif mode == 'int':
        tmp = readInt(string, color)
    print('\033[m', end = '')
    return tmp


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


# Functions that reads and formats data for the student

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

    birthDay.setDay(day)
    birthDay.setMonth(month)
    birthDay.setYear(year)

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
    gender = inputf("Gender(F/M): ").strip().upper()
    if(gender == ''):
        printf(f"Gender can't be left blank. Try again.", 'red', 'underline')
        return readGender() 
    gender = gender[0]
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
        return readName()
    elif len(name) < 5:
        printf('THE NAME MUST CONTAIN AT LEAST FIVE(5) LETTERS! TRY AGAIN!', 'red', 'underline')
        return readName()
    name = name.title()
    printf(f"'{name}' Was defined as the name.", 'blue', 'underline')
    return name
        

def searchStudent(target = str(), studentList = []):
    for student in studentList:
        if student.getCode() == target:
            return student
        

def validateStudent(target = str(), studentList = []):
    for student in studentList:
        if student.getCode() == target:
            return True
    return False


# Print functions

def printMenu(studentsList):
    if(len(studentsList) == 0):
        printf('There are no students to show righ now. Come back later...', 'red', 'underline')
    
    tittle('LIST MENU', '-', 'blue')
    print('[0] - BACK')
    print('[1] - SORT BY AGE')
    print('[2] - SORT BY DEFAULT')
    print('[3] - SORT BY NAME')
    tittle('LIST MENU', '-', 'blue', True)
    printMenuChoice = inputf('Your choice: ')
    switch (escolha_menu_listagem)

def printList(studentsList = []):
    tittle('LISTING STUDENTS', '=', 'green')
    for index in range (0, len(studentsList)):
        printPerson(index, studentsList[index])
        if not index == len(studentsList) - 1:
            tittle('LISTING STUDENTS', '=', line = True)


def sortByName(studentsList):
    tmp = sorted(studentsList, key = lambda student: student.name)
    printList(tmp)


def sortByAge(studentsList):
    tmp = sorted(studentsList, key = lambda student: student.age)
    printList(tmp)

