from tkinter import *
'''rows and colomns to arrange info'''
root = Tk()

label_1 = Label(root, text='FirstName', bg='Red', fg='White')
label_1.pack(fill=X)

label_2 = Label(root, text='Second Name', bg='Blue', fg='White')
label_2.pack(side=RIGHT,fill=Y)



root.mainloop()
