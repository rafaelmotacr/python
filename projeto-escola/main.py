from modulo import *

# Main

quit = False
studentsList = []
 
day = personDate()
day.setDay(9)
day.setMonth(1)
day.setYear(2003)
rafael = student()
rafael.setName('Rafael')
rafael.setBirthday(day)
rafael.setGender('Helicoptero')
rafael.setAge()
rafael.setCpf('187.345.287-78')
rafael.setCode(1)
studentsList.append(rafael)

day = personDate()
day.setDay(8)
day.setMonth(12)
day.setYear(1985)
rafael = student()
rafael.setName('Elias')
rafael.setBirthday(day)
rafael.setGender('Caruru')
rafael.setAge()
rafael.setCpf('125.355.661-12')
rafael.setCode(2)
studentsList.append(rafael)


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
        print('UPDATE')
    elif choice == '4':
        sortByName(studentsList)
        #printStudents(studentsList)
    else:
        tittle(f'INVALID OPTION!', '~', 'red')
