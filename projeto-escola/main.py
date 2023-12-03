from modulo import *

# Main

quit = False

while(not quit):
    mainMenu()
    choice = input('> Your Choice: ')
    if(choice == '1'):
        #createstudent()
        readName()
        readGender()
        print('CREATE')
    elif(choice == '2'):
        #removestudent()
        print('REMOVE')
    elif(choice == 3):
        #updateStudent()
        print('UPDATE')
    elif(choice == '4'):
        #viewsStudents:()
        print('VIEW')
    else:
        tittle(f'INVALID OPTION!', '~', 'red')
