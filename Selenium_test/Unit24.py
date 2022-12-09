# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://google.com')
# driver.quit()

from pywinauto.application import Application
# Запускаем целевое приложение - обычный блокнот
app = Application().start("notepad.exe")
# Выбираем пункт меню
app.UntitledNotepad.menu_select("Справка->О программе")
# Симулируем клик
app.AboutNotepad.OK.click()
# Вводим текст
app.UntitledNotepad.Edit.type_keys("Заработало!", with_spaces = True)