from modulo import *

# Main

quit = False
studentsList = []
 
while (not quit):
    choice = mainMenu()
    if choice == '0': 
        tittle('LEAVING..','=', 'red')
        quit = True
        break
    if choice == '1':
        createStudent(studentsList)
        print('CREATE')
    elif choice == '2':
        #removestudent()
        print('REMOVE')
    elif choice == 3:
        #updateStudent()
        print('UPDATE')
    elif choice == '4':
        for i in range (0, len(studentsList)):
            print(f'{i + 1} - ', end = '')
            student.toString()
        print('VIEW')
    else:
        tittle(f'INVALID OPTION!', '~', 'red')
