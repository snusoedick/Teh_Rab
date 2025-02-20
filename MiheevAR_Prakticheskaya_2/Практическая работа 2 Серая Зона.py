import tkinter as tk
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton

window = tk.Tk()
window.title("Рассказ")
window.geometry('400x350')

selected = tk.IntVar()

lbl = tk.Label(window, text="Отрывок из 'Евгений Онегин'", font=("Arial", 12))
lbl.grid(column=0, row=0, padx=10, pady=10)

txt = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
txt.insert(tk.END, """I
«Мой дядя самых честных правил,
Когда не в шутку занемог,
Он уважать себя заставил
И лучше выдумать не мог.
Его пример другим наука;
Но, боже мой, какая скука
С больным сидеть и день и ночь,
Не отходя ни шагу прочь!
Какое низкое коварство
Полуживого забавлять,
Ему подушки поправлять,
Печально подносить лекарство,
Вздыхать и думать про себя:
Когда же черт возьмет тебя!»
II
Так думал молодой повеса,
Летя в пыли на почтовых,
Всевышней волею Зевеса
Наследник всех своих родных.
Друзья Людмилы и Руслана!
С героем моего романа
Без предисловий, сей же час
Позвольте познакомить вас:
Онегин, добрый мой приятель,
Родился на брегах Невы,
Где, может быть, родились вы
Или блистали, мой читатель;
Там некогда гулял и я:
Но вреден север для меня 1.
III
Служив отлично благородно,
Долгами жил его отец,
Давал три бала ежегодно
И промотался наконец.
Судьба Евгения хранила:
Сперва Madame за ним ходила,
Потом Monsieur ее сменил.
Ребенок был резов, но мил.
Monsieur l'Abbé, француз убогой,
Чтоб не измучилось дитя,
Учил его всему шутя,
Не докучал моралью строгой,
Слегка за шалости бранил
И в Летний сад гулять водил.
""")
txt.grid(column=0, row=1, padx=10, pady=10)

rad_frame = tk.Frame(window)
rad_frame.grid(row=2, column=0, columnspan=2, pady=5)

rad1 = Radiobutton(rad_frame, text='Читал', value=1, variable=selected)
rad2 = Radiobutton(rad_frame, text='Буду читать', value=2, variable=selected)

rad1.grid(column=0, row=0, padx=10)
rad2.grid(column=1, row=0, padx=10)

window.mainloop()