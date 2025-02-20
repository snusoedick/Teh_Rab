from tkinter import * # (Подгружаем визуальные контролы)
from tkinter.ttk import Combobox # (Использование класса для добавления виджета)
from tkinter.ttk import Checkbutton # (Использование класса для добавления виджета)

window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

chk_state = BooleanVar() # (Тип переменной)
chk_state.set(True) # (Состояние чекбокса)
chk = Checkbutton(window, text='Выбрать', var=chk_state) # (Создание виджета checkbutton)
chk.grid(column=0, row=0) # (Установка позиции в окне)

combo = Combobox(window) # (Создание поля с выпадающим списком combobox)
combo['values'] = (1, 2, 3, 4, 5, "Текст") # (Значения в combobox)
combo.current(1) # Вариант по умолчанию
combo.grid(column=1, row=0) # (Установка позиции в окне)

window.mainloop()# (Ожидание действия пользователя)
