from tkinter import *

def window_resolution():
    print(root.winfo_width())
    print(root.winfo_height())


def create():
   
    # destruição

   label1.destroy()
   label2.destroy()
   create_button.destroy()
   sort_button.destroy()
   root.destroy()
   janela2 = Tk()
    # criação

   title_name = Label()
   title_name['text'] = 'Name:'
   title_name['font'] = 'comic 10'
   title_name.grid(column = 0, row = 0)

   name = Entry()
   name.grid(column = 1, row = 0, sticky = 'WE')

   confirmation_button = Button()
   confirmation_button['text'] = 'Confirm'
   confirmation_button['font'] = 'comic 10'
   confirmation_button.grid(column = 2, row = 0, sticky = 'WE')

   back_button = Button()
   back_button['text'] = 'Back'
   back_button['font'] = 'comic 10'
   back_button.grid(column = 0, row = 1, sticky = 'WE')


def sort_features():
    window_resolution()


root = Tk()
#root.iconbitmap(r"C:\Users\tiubo\Documents\Cursos\Projeto_Valasque\pictures\megamind.ico")
root.title("Criador de Chars")


# PC resolution

width_sys = root.winfo_screenwidth()
height_sys = root.winfo_screenheight()

# Window resolution before evalute 

width_window = 262
height_window = 99 # antes era 127

# Window position

xpos = width_sys // 2 - width_window // 2
ypos = height_sys // 2 - height_window // 2

# Window configs 

root.geometry(f'{width_window}x{height_window}+{int(xpos)}+{int(ypos)}')
root.resizable(width = 0, height = 0)
root.state('normal')

# Label 1

label1 = Label(master= root)
label1['text'] ='Character Creator'
label1['font'] = 'comic 12 bold'
label1['justify'] ='center'
label1['relief'] ='groove'
label1['border'] = 2
label1.grid(columnspan = 2, sticky= 'WE')

# Label 2

label2 = Label(master= root)
label2['text'] ='Welcome to my program! \nChoose an option to begin!'
label2['font'] = 'comic 12'
label2['bg'] = 'light blue'
label2['justify'] ='left'
label2['relief'] ='groove'
label2['border'] = 2
label2.grid(columnspan = 2, sticky= "WE")

# Button 1

create_button = Button(master = root)
create_button['text'] = 'Create from zero'
create_button['command'] = command= lambda:create()
create_button['font'] = font = 'comic 12'
create_button.grid(column = 0, row = 2, sticky= "WE")

# Button 2

sort_button = Button(master = root)
sort_button['text'] = 'Sort out Features'
sort_button['command'] = command = lambda:sort_features()
sort_button['font'] = font = 'comic 12'
sort_button.grid(column = 1, row = 2, sticky= "WE")

root.mainloop()
