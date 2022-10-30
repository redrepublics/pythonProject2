from tkinter import *
import tkinter as tk

window = tk.Tk()

root = Tk()  # создаем корневой объект - окно
root.title("db_tools v.1.0.0.1")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна

label = Label(text="Программа обслуживания базы данных АСПО")  # создаем текстовую метку
button = tk.Button(
    text="ЗАПУСТИТЬ",
    width=30,
    height=30,
    bg="blue",
    fg="yellow",
)
label.pack()  # размещаем метку в окне
button.pack()



window.mainloop()



