def tittle(string, char, color = "NULL", line = False):

    colors =  {
        'gray':'\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'ligth-blue': '\033[36m',
    }

    if(not line):
        print(f'{char}' * (len(string) + 4))
        print(f'{colors[color]}  {string}  \033[m')
        print(f'{char}' * (len(string) + 4))
    else:
        print(f'{char}' * (len(string) + 4))


def mainMenu():
    tittle("MAIN MENU", '=', 'blue')
    print('[0] - QUIT')
    print('[1] - CREATE STUDENT')
    print('[2] - REMOVE STUDENT')
    print('[3] - UPDATE STUDENT')
    print('[4] - VIEW STUDENTS')
    tittle("MAIN MENU", '=', line = True)


class student:
    def __init__(self,name = "No name", age = 0, code = "NULL", cpf = "NULL", sex = "NULL" ):
        self.name = name
        self.age = age
        self.code = code
        self.cpf = cpf
        self.sex = sex


    def setName(self,name):
        self.name = name
    

    def setAge(self,age):
        self.age = age


    def setCode(self, code):
        self.code = code


    def setCpf(self, cpf):
        self.cpf = cpf

    
    def setCpf(self, cpf):
        self.cpf = cpf


# Main

quit = False

while(not quit):
    mainMenu()
    choice = int(input("> Your Choice: "))
    switch(choice):
    
