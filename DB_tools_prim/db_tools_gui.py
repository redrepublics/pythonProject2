import os
import sys

from tkinter import *
import tkinter.ttk as ttk


x = os.getcwd()
y = 'FontAwesome_f085(0).ico'
window = Tk()
window.iconbitmap(os.path.join(x, y))
window.title("DB Tools v.1.0.0.1")
window.geometry('350x250')

txtarea = Text(window, width=45, height=10)
# txtarea.place(x=150, y=120, anchor="c")
txtarea.bind("<Key>", lambda e: "break")
txtarea.place(relx=0.5, rely=0.5, anchor="c", relwidth=0.7, relheight=0.7)


def run():
    os.system('python start_db.py')


def run2():
    sys.exit(1)


ttk.Button(window, text="Старт", command=run).place(relx=0.3, rely=0.01)
ttk.Button(window, text="Выход", command=run2).place(relx=0.5, rely=0.01)
# btn.grid(column=0, row=0)
# btn2.grid(column=15, row=0)

window.mainloop()
