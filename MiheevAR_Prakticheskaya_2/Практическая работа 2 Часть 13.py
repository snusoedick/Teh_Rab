from tkinter import * # (Подгружаем визуальные контролы)
from tkinter import Menu 

window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать !!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

menu = Menu(window) # (Панель меню)
new_item = Menu(menu) # (Панель меню)
new_item.add_command(label='Новый') # (Текст в панели)
menu.add_cascade(label='Файл', menu=new_item) # (Текст в подменю) 
window.config(menu=menu) # (Расположение)

window.mainloop() # (Ожидание действия пользователя)
