import tkinter as tk
from tkinter import ttk

def update_progress():
    try:
        value = int(entry.get())
        if 0 <= value <= 100:
            progress_bar['value'] = value
            status_label.config(text=f"Вами установлено: {value} %")
        else:
            status_label.config(text="Введите число от 0 до 100")
    except ValueError:
        status_label.config(text="Введите корректное число")

window = tk.Tk()
window.title("Прогресс")
window.geometry('300x150')

title_label = tk.Label(window, text="Прогресс ради прогресса", font=("Arial", 12))
title_label.grid(column=0, row=0, pady=10)

style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", background='green')

progress_bar = ttk.Progressbar(window, length=300, style='green.Horizontal.TProgressbar')
progress_bar.grid(column=0, row=1, pady=10)

input_frame = tk.Frame(window)
input_frame.grid(row=2, column=0, pady=5)

entry = tk.Entry(input_frame, width=10)
entry.grid(column=0, row=0, padx=5)

instruction_label = tk.Label(input_frame, text="Укажите количество процентов", font=("Arial Bold", 12))
instruction_label.grid(column=1, row=0)

update_button = tk.Button(window, text="Ok", command=update_progress)
update_button.grid(column=0, row=3, pady=10)

status_label = tk.Label(window, text="Вами установлено: 0%", font=("Arial Bold", 18))
status_label.grid(column=0, row=4, pady=10)

window.mainloop()

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Python File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": (True)
        }
    ]
}