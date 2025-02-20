from tkinter import * # (Подгружаем визуальные контролы)
from tkinter.ttk import Progressbar # (Использование класса для добавления виджета)
from tkinter import ttk

window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать в приложение PythonRu") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

style = ttk.Style() # (Стиль полосы загрузки)
style.theme_use('default') # (Стиль оглавления)
style.configure("black.Horizontal.TProgressbar", background='red') # (Цвет полосы)

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar') # (Создание полосы progressbar)
bar['value'] = 70 # (Значение) 
bar.grid(column=0, row=0) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
