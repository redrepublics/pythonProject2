# from tkinter import *
# import tkinter as tk
#
#
# def click_button():
#     # изменяем текст на кнопке
#     # button["text"] = f"Clicks {clicks}"
#     print("Ура")
#
#
#
# window = tk.Tk()
# window.title("Обслуживание баз АСПО v.1.0.0.2")
# window.geometry("300x200")
# label = tk.Label(text="ЗАПУСК")
# entry = tk.Entry()
# button = tk.Button(
#     text="Нажми на меня!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
#     command=click_button
# )
# label.pack()
# button.pack()
# window.mainloop()
#
#
#
#maincode.py

import os
import sys
import subprocess
from tkinter import *

window = Tk()

window.title("Running Python Script")
window.geometry('550x200')


txtarea = Text(window, width=25, height=10)
txtarea.place(x=250, y=95, anchor="c")
txtarea.bind("<Key>", lambda e: "break")


def run():
    os.system('db_tools.py')


btn = Button(window, text="Running Script", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()