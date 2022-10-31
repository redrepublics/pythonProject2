import os

from tkinter import *
x = os.getcwd()
y = 'FontAwesome_f085(0).ico'
window = Tk()
window.iconbitmap(os.path.join(x, y))
window.title("Обслуживание баз АСПО")
window.geometry('550x200')

txtarea = Text(window, width=45, height=10)
txtarea.place(x=250, y=95, anchor="c")
txtarea.bind("<Key>", lambda e: "break")


def run():
    os.system('python db_tools.py')


btn = Button(window,  text="START",  command=run)
btn.grid(column=0, row=0)

window.mainloop()
