from tkinter import * # (Подгружаем визуальные контролы)
from tkinter.ttk import Radiobutton # (Использование класса для добавления виджета)

def clicked(): # (Функция на клик)
    lbl.configure(text=selected.get()) # (Вывод текста в окне)
    
window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

selected = IntVar() # (Тип переменной)

rad1 = Radiobutton(window, text='Первый', value=1, variable=selected) # (Создание radio кнопки)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected) # (Создание radio кнопки)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected) # (Создание radio кнопки)

btn = Button(window, text="Клик", command=clicked) # (Добавление кнопки)
lbl = Label(window) # (Добавление Текстового элемента)

rad1.grid(column=0, row=0) # (Установка позиции в окне)
rad2.grid(column=1, row=0) # (Установка позиции в окне)
rad3.grid(column=2, row=0) # (Установка позиции в окне)

btn.grid(column=3,row=0) # (Установка позиции в окне)
lbl.grid(column=0, row=1) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
