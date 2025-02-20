from tkinter import * # (Подгружаем визуальные контролы)
from tkinter import scrolledtext # (Использование класса для добавления виджета)

window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

txt = scrolledtext.ScrolledText(window, width=40, height=10) # (Создание текстового элемента scrolledtext)
txt.grid(column=0, row=0) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
