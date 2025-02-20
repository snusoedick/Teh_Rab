from tkinter import * # (Подгружаем визуальные контролы)
from tkinter import messagebox # (Использование класса для добавления виджета)

def clicked(): # (Функция на клик)
    messagebox.showinfo('Заголовок', 'Текст') # (Вывод сообщения на всплывающее окно)
    
window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

btn = Button(window, text='Клик', command=clicked) # (Создание кнопки)
btn.grid(column=0, row=0) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
