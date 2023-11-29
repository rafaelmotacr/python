from datetime import datetime
from random import randint
from tkinter import *
from pyperclip import copy

def show_date():
    month = randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month == 2:
        day = randint(1, 29)
    else:
        day = randint(1, 30)
    result.set(f"Sorted date: {day:0>2}/{month:0>2}.")
    label2.grid(columnspan = 2)


def copy_text():
    copy(str(result.get())[13:19])
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
root.config(bg = 'white')

greeting = StringVar()
greeting.set(hour_set())
result = StringVar()

label1 = Label(master = root, textvariable = greeting)
label1['bg'] = 'cyan'
label1['fg'] = 'black'
label1['font'] = 'comic 10'
label1['bd'] = 2
label1['relief'] = 'groove'
label1.grid(columnspan = 2)

label2 = Label(master = root, textvariable = result)
label2['bg'] = 'white'
label2['font'] = 'comic 10'
label2['fg'] = 'black'
label2.grid(columnspan = 2)

btcreat = Button(master = root)
btcreat['text'] = 'Sort Date'
btcreat['bg'] = 'cyan'
btcreat['fg'] = 'black'
btcreat['font'] = 'comic 10'
btcreat['command'] = show_date
btcreat.grid(column = 0, row = 2, sticky = 'WE')

btcopy = Button(master = root)
btcopy['text'] = 'Copy text'
btcopy['bg'] = 'cyan'
btcopy['fg'] = 'black'
btcopy['font'] = 'comic 10'
btcopy['command'] = copy_text
btcopy.grid(column = 1, row = 2, sticky = 'WE')

root.mainloop()
