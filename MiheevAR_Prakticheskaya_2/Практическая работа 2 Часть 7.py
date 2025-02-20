from tkinter import * # (Подгружаем визуальные контролы)
from tkinter.ttk import Radiobutton # (Использование класса для добавления виджета)

window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

rad1 = Radiobutton(window, text='Первый', value=1) # (Создание radio кнопки)
rad2 = Radiobutton(window, text='Второй', value=2) # (Создание radio кнопки)
rad3 = Radiobutton(window, text='Третий', value=3) # (Создание radio кнопки)
rad1.grid(column=0, row=0) # (Установка позиции в окне)
rad2.grid(column=1, row=0) # (Установка позиции в окне)
rad3.grid(column=2, row=0) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
