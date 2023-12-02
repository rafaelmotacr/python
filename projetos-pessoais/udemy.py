# Name: Udemy.
# Objective: The program switch between accounts on the udemy platform.
# Creator: Rafael Mota.
# Creation date: 18/03/2023.

import pyautogui 
import pyperclip
import time

def read_int(msg):
    while True:
        num = input(msg)
        try:
            exit = int(num)
        except:
            print('\033[31m> This is not an integer, try again!\033[m\n')
        else:
            return int(num)


def acess_link(link, guide = False, email = False):
    if guide:
        pyautogui.hotkey('ctrl','t')
    pyperclip.copy(link)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    if email:
        pyautogui.hotkey('ctrl','enter')


def select_course(courses, format = list()):
    while True:
        print('\n\033[30;40m> Which course do you want to use?\033[m')
        for index, value in enumerate (courses):
            print(f'\033[33m{index + 1}\033[m - {format[index]}{value}\033[m course.')
        choice = read_int('\033[30;40m> You answer: \033[31m') - 1  
        if choice >= len(courses) or choice < 0:
            print('\033[31m> Invalid option! Try again!\033[m')
        else:
           print(f'\033[m> The {format[choice]}{courses[choice]}\033[m course is selected!')
           return choice
        

def select_account(num):
    xpos = 626
    ypos = 410
    if num > 0:
        for increase in range(0, num):
            ypos += 66
    pyautogui.click(x = xpos,y =ypos)
 
pyautogui.PAUSE = 1
options = ['java', 'Excel','Python','Nets']
collors = ['\033[31m','\033[32m','\033[35m', '\033[36m']
controll = select_course(courses = options, format = collors )
pyautogui.press("win") # Press the windows key
pyautogui.write("chrome") # Write "chrome" in the windows bar 
pyautogui.press("enter") # Open "chrome" 
time.sleep(1)
acess_link(r"https://www.udemy.com/", True) # Acess "udemy" site
pyautogui.moveTo(x = 1300 , y = 132, duration = 4) # Drag to "profile" on "udemy"
pyautogui.press("pagedown") # Scroll down until "exit" is visible
pyautogui.click(x = 1269, y = 369) # Press "exit"
time.sleep(7) 
pyautogui.click(x = 1110, y = 138) # Press the button to loguin 
time.sleep(5)
pyautogui.click(x = 730, y = 486) # chose "login into another account"
time.sleep(5)
pyautogui.click(x = 738, y = 279) # Choose google login method 
time.sleep(10)
select_account(controll) # Choose wich account to use 
time.sleep(5)
pyautogui.moveTo(x = 1300 , y = 132, duration = 4) # Drag to "profile" on "udemy"
pyautogui.click(x = 1147, y = 293) # Select my learning tab 
time.sleep(5)
pyautogui.click(x = 344, y = 426) # Click on the selectd course 
time.sleep(15)
pyautogui.alert(rf'The {options[controll]} course is now open!')
