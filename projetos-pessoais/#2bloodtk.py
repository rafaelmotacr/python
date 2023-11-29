from datetime import datetime
from random import randrange
from tkinter import *
from pyperclip import copy

def show_blood():
    blood = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'];
    result.set(f"Sorted blood: {blood[randrange(len(blood))]}.")
    label2.grid(columnspan = 2)


def copy_text():
    copy(str(result.get())[14:19])
    print('Texto copiado!')


def hour_set():

    hour = int(datetime.now().strftime("%H"))
    text = "> Good night, master!"
    if hour < 12:
        text = "> Good morning, master!"
    elif 12 <= hour < 18:
        text = "> Good afternoon, master!"
    return text


root = Tk()
root.config(bg = 'grey8')
root.resizable(0,0)

greeting = StringVar()
greeting.set(hour_set())
result = StringVar()

label1 = Label(master = root, textvariable = greeting)
label1['bg'] = 'red'
label1['fg'] = 'white'
label1['bd'] = 2
label1['relief'] = 'groove'
label1.grid(columnspan = 2)

label2 = Label(master = root, textvariable = result)
label2['bg'] = 'grey8'
label2['fg'] = 'white'
label2.grid(columnspan = 2)

btcreat = Button(master = root)
btcreat['text'] = 'Sort Blood'
btcreat['bg'] = 'red'
btcreat['fg'] = 'white'
btcreat['command'] = show_blood
btcreat.grid(column = 0, row = 2, sticky = 'WE')

btcopy = Button(master = root)
btcopy['text'] = 'Copy text'
btcopy['bg'] = 'red'
btcopy['fg'] = 'white'
btcopy['command'] = copy_text
btcopy.grid(column = 1, row = 2, sticky = 'WE')

root.mainloop()
