from tkinter import * #(Подгружаем визуальные контролы)

def clicked(): # (Функция, срабатывающая при нажатии кнопки)
    lbl.configure(text="Я же просил...") # (Изменение текста в label после срабатывания функции)
    
window = Tk() # (Вызываем библиотеку графических элементов)
window.title("Добро пожаловать!!!") # (Заголовок окна)
window.geometry('400x250') # (Установка размера окна)

lbl = Label(window, text="Привет", font=("Arial Bold",50)) # (Создание текстового элемента Label)
lbl.grid(column=0, row=0) # (Установка позиции в окне)

btn = Button(window, text="Не нажимать!", bg="black", fg="white", command=clicked) # (Добавление кнопки)
btn.grid(column=1, row=0) # (Расположение кнопки)

window.mainloop() # (Ожидание действия пользователя)

