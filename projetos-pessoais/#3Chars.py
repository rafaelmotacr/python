# Criador de chars em Python

from random import *
from datetime import *
import os
import tkinter

class Character:
    def __init__(self):
        os.system('cls')
        self.id = f"{date.today().day}{date.today().month}{date.today().year}{randint(10, 100)}"
        print(f"\033[30;40m* Character id is: {self.id}.\033[m\n")
        self.set_date()
        self.set_sex()
        self.set_blood()
        self.set_skin()


    def set_date(self):
        month = randint(1, 12)
        if month == 2:
            day = randint(1, 28)
        else:
            day = randint(1, 31)
        self.date = f"{day:0>2}/{month:0>2}"


    def set_sex(self):
        options = ['Masculine', 'Feminine']
        self.sex = options[randrange(len(options))]

    def set_blood(self):
        options = ['A+', 'A-','B+', 'B-', 'AB+', 'Ab-', 'O+', 'O-']
        self.blood = options[randrange(len(options))]


    def set_skin(self):
        options = ['Black', 'White','Yelow', 'Brow']
        self.skin = options[randrange(len(options))]


    def get_name(self):
        valid = False
        while not valid:
            self.name = input('\033[30;40m> Write character name:\033[m')
            for char in self.name:
                if not char.isalpha():
                    valid = False
                    print("> The name have to contain only alphabet letters! Try again!")
                    break
                valid = True
        self.name = self.name.title()


def tittle(string, collor = '\033[m', line = False):
    if line:
        print("-" * (len(string) + 4))
    else:
        print("-" * (len(string) + 4))
        print(f"  {collor}{string}\033[m")
        print("-" * (len(string) + 4))


cont = 0
options = ['Create from zero', 'Sort out some features']
collors = {'clean':"\033[m",
    'black':"\033[30m",
    'red':"\033[31m", 
    'green':"\033[32m",
    'yellow':"\033[33m",
    'blue':"\033[34m",
    'purple':"\033[35m",
    'light blue':"\033[36m"}


while True:
    tittle(f"Char Creator", f"{collors['purple']}")
    for index, value in enumerate (options):
        print(f"{collors['blue']}{index + 1}{collors['clean']} - {collors['green']}{value}{collors['clean']}.")
    while True:
        tittle("your choice", line = True)
        choice = int(input(f"{collors['blue']}> {collors['purple']}Your choice: {collors['clean']}"))
        if choice > len(options):
            print(f"{collors['blue']}> {collors['red']}Invalid option, try again!")
            continue
        break
    if choice == 1:
        Sabrina =  Character()
        Sabrina.get_name()
        informacoes = {'Name': f"{Sabrina.name}", 
                       'Birthday': f"{Sabrina.date}",
                        'Blood Type': f"{Sabrina.blood}", 
                        'Skin color': f"{Sabrina.skin}", 
                        'Sex': f"{Sabrina.sex}"}
        tittle("Character informations", collor="\033[32;40m")
        print()
        for i, j in informacoes.items():
            cont += 1
            print(f"  {collors['yellow']}{cont}{collors['clean']} - {collors['purple']}{i}{collors['clean']} = {collors['green']}{j}{collors['clean']}.")
        quit = input("\n\033[30;40m> Deseja continuar no programa?")

    elif choice == 2:
        print("bad")


 

 