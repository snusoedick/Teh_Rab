import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser

def create_collage(images, output_file, title_text, bg_color='grey', cell_width=200, cell_height=200, border_size=10, frame_color=None, frame_thickness=0):
    if not images:
        messagebox.showerror("Ошибка", "Не выбраны изображения.")
        return

    # Приветственный текст
    font_size = 30
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Определение размера коллажа
    num_images = len(images)
    cols = int(num_images ** 0.5)  # Количество колонок
    rows = (num_images + cols - 1) // cols  # Количество строк

    collage_width = cols * cell_width + (cols + 1) * border_size
    collage_height = rows * cell_height + (rows + 1) * border_size + font_size + border_size

    # Создание фона коллажа
    collage = Image.new('RGB', (collage_width, collage_height), color=bg_color)
    draw = ImageDraw.Draw(collage)

    # Добавление заголовка
    text_width, text_height = draw.textbbox((0, 0), title_text, font=font)[2:4]
    draw.text(((collage_width - text_width) / 2, border_size), title_text, fill="black", font=font)

    # Обработка изображений
    x_offset = border_size
    y_offset = border_size + font_size + border_size

    for img_path in images:
        img = Image.open(img_path)

        # Определение ориентации изображения
        if img.width > img.height:  # Альбомная ориентация
            img = ImageOps.fit(img, (cell_width, cell_height), Image.LANCZOS)
        else:  # Портретная ориентация
            img = ImageOps.fit(img, (cell_height, cell_width), Image.LANCZOS)

        # Добавление рамки (если указана)
        if frame_color and frame_thickness > 0:
            img = ImageOps.expand(img, border=frame_thickness, fill=frame_color)

        # Вставка изображения на коллаж
        collage.paste(img, (x_offset, y_offset))

        # Переход к следующей позиции
        x_offset += cell_width + border_size

        if x_offset + cell_width > collage_width:  # Переход на следующую строку
            x_offset = border_size
            y_offset += cell_height + border_size

    # Сохранение коллажа
    collage.save(output_file)
    messagebox.showinfo("Успех", f"Коллаж сохранён в файл: {output_file}")

def select_images(num_images, image_labels, file_paths):
    for i in range(num_images):
        file_path = filedialog.askopenfilename(title=f"Выберите изображение {i+1}", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            file_paths[i] = file_path
            image_labels[i].config(text=os.path.basename(file_path))

def main():
    root = tk.Tk()
    root.title("Создание коллажа")

    # Запрос заголовка
    title_text = simpledialog.askstring("Заголовок", "Введите заголовок для коллажа:", parent=root)
    if not title_text:
        messagebox.showerror("Ошибка", "Заголовок не введен.")
        return

    # Запрос количества изображений
    num_images = simpledialog.askinteger("Количество изображений", "Введите количество изображений (от 2 до 10):", parent=root, minvalue=2, maxvalue=10)
    if not num_images:
        messagebox.showerror("Ошибка", "Количество изображений не введено.")
        return

    # Переменные для настроек коллажа
    bg_color = 'grey'  # Цвет фона по умолчанию
    cell_width = 200   # Ширина ячейки по умолчанию
    cell_height = 200  # Высота ячейки по умолчанию
    frame_color = None  # Цвет рамки (по умолчанию отсутствует)
    frame_thickness = 0  # Толщина рамки (по умолчанию отсутствует)

    # Функция для выбора цвета фона
    def choose_bg_color():
        nonlocal bg_color
        color = colorchooser.askcolor(title="Выберите цвет фона")[1]  # Возвращает кортеж (RGB, HEX)
        if color:
            bg_color = color
            bg_color_btn.config(bg=color)

    # Функция для выбора цвета рамки
    def choose_frame_color():
        nonlocal frame_color
        color = colorchooser.askcolor(title="Выберите цвет рамки")[1]
        if color:
            frame_color = color
            frame_color_btn.config(bg=color)

    # Создание интерфейса для выбора изображений
    file_paths = [None] * num_images
    image_labels = []

    for i in range(num_images):
        frame = tk.Frame(root)
        frame.pack(fill=tk.X, padx=5, pady=5)
        btn = tk.Button(frame, text=f"Выбрать изображение {i+1}", command=lambda i=i: select_images(num_images, image_labels, file_paths))
        btn.pack(side=tk.LEFT)
        label = tk.Label(frame, text="Файл не выбран")
        label.pack(side=tk.LEFT, padx=5)
        image_labels.append(label)

    # Поля для ввода размера ячеек
    cell_size_frame = tk.Frame(root)
    cell_size_frame.pack(pady=10)
    tk.Label(cell_size_frame, text="Ширина ячейки:").pack(side=tk.LEFT)
    cell_width_entry = tk.Entry(cell_size_frame, width=5)
    cell_width_entry.insert(0, "200")
    cell_width_entry.pack(side=tk.LEFT, padx=5)
    tk.Label(cell_size_frame, text="Высота ячейки:").pack(side=tk.LEFT)
    cell_height_entry = tk.Entry(cell_size_frame, width=5)
    cell_height_entry.insert(0, "200")
    cell_height_entry.pack(side=tk.LEFT, padx=5)

    # Кнопка для выбора цвета фона
    bg_color_btn = tk.Button(root, text="Выбрать цвет фона", command=choose_bg_color, bg=bg_color)
    bg_color_btn.pack(pady=10)

    # Кнопка для выбора цвета рамки
    frame_color_btn = tk.Button(root, text="Выбрать цвет рамки", command=choose_frame_color, bg="white")
    frame_color_btn.pack(pady=5)

    # Поле для ввода толщины рамки
    frame_thickness_frame = tk.Frame(root)
    frame_thickness_frame.pack(pady=5)
    tk.Label(frame_thickness_frame, text="Толщина рамки:").pack(side=tk.LEFT)
    frame_thickness_entry = tk.Entry(frame_thickness_frame, width=5)
    frame_thickness_entry.insert(0, "0")
    frame_thickness_entry.pack(side=tk.LEFT, padx=5)

    # Кнопка создания коллажа
    def on_create():
        nonlocal cell_width, cell_height, frame_thickness
        try:
            cell_width = int(cell_width_entry.get())
            cell_height = int(cell_height_entry.get())
            frame_thickness = int(frame_thickness_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректные значения для размера ячейки или толщины рамки.")
            return

        images = [fp for fp in file_paths if fp is not None]
        if len(images) < 2:
            messagebox.showerror("Ошибка", "Необходимо выбрать как минимум два изображения.")
            return
        output_file = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")], title="Сохранить коллаж как")
        if output_file:
            create_collage(images, output_file, title_text, bg_color, cell_width, cell_height, border_size=10, frame_color=frame_color, frame_thickness=frame_thickness)

    create_btn = tk.Button(root, text="Создать коллаж", command=on_create)
    create_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()