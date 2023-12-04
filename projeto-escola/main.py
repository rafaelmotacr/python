from modulo import *

# Main

quit = False
defaultcode = f'{datetime.now().year}{datetime.now().month}'

while(not quit):
    mainMenu()
    choice = input('> Your Choice: ')
    if choice == '0': 
        tittle('LEAVING..','=', 'red')
        quit = True
        break
    if choice == '1':
        oi = readCPF()
        print('CREATE')
    elif choice == '2':
        #removestudent()
        print('REMOVE')
    elif choice == 3:
        #updateStudent()
        print('UPDATE')
    elif choice == '4':
        #viewsStudents:()
        print('VIEW')
    else:
        tittle(f'INVALID OPTION!', '~', 'red')
