from tkinter import *

root = Tk()

def dosomething():
    print('clicked a button')

button_1 = Button(root, text='click here', command=dosomething)
button_1.pack()

root.mainloop()
