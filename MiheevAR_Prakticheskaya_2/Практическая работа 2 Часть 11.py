from tkinter import * # (Подгружаем визуальные контролы)
from tkinter import messagebox # (Использование класса для добавления виджета)

def clicked(): # (Функция на клик)
    messagebox.showinfo('Заголовок', 'Текст') # (Вывод сообщения на всплывающее окно)
    
window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

spin = Spinbox(window, from_=0, to=100, width=5) # (Создание виджета spinbox)
spin.grid(column=0, row=0) # (Установка позиции в окне)

window.mainloop() # (Ожидание действия пользователя)
