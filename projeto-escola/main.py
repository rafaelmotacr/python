from modulo import *

# Main

quit = False
studentsList = []

while not quit:
    choice = mainMenu()
    if choice == '0': 
        tittle('LEAVING..','=', 'red')
        quit = True
        continue
    elif choice == '1':
        createStudent(studentsList)
    elif choice == '2':
        removeStudent(studentsList)
    elif choice == '3':
        updateCentral(studentsList)
    elif choice == '4':
        printCentral(studentsList)
    else:
        tittle(f'INVALID OPTION!', '~', 'red')
