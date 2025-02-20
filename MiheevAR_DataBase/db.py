import pyodbc
from tkinter import*
from tkinter import messagebox

#Параметры подключения к базе данных
server = '02-Server' #Имя сервера иди IP-адрес
database = 'RPM' #Имя базы данных
username = '02-Student1' #Имя пользователя
password = '02-Zcneltyn' #Пароль

#Создаем строку подключения
connection_string = ("DRIVER={ODBC Driver 17 for SQL Server};" "SERVER=02-Server;" "DATABASE=RPM;" "Trusted_Connection=yes;")

#Функция для подключения к базе данных
def connect_to_bd():
    try:
        conn = pyodbc.connect(connection_string)
        print("Подключение к базе данных успешно установлено.")
        return conn
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

# Функция для создания таблицы, если она не существует
def create_table(conn):
    cursor = conn.cursor()
    create_table_query = """
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Products')
    BEGIN
        CREATE TABLE Products (
            ProductID INT PRIMARY KEY IDENTITY(1,1),
            ProductName NVARCHAR(100) NOT NULL,
            Category NVARCHAR(50),
            Price DECIMAL(10, 2),
            Quantity INT
        )
    END
    """
    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица 'Products' создана (если не существовала).")
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")

# Функция для добавления продукта в базу данных
def add_product_to_db(product_name, category, price, quantity, conn):
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Products (ProductName, Category, Price, Quantity)
    VALUES (?, ?, ?, ?)
    """
    try:
        cursor.execute(insert_query, (product_name, category, price, quantity))
        conn.commit()
        messagebox.showinfo("Успех", "Продукт успешно добавлен!")
    except Exception as e:
        print(f"Ошибка при добавлении продукта: {e}")
        messagebox.showerror("Ошибка", f"Не удалось добавить продукт: {e}")

# Функция для обработки нажатия кнопки "Добавить"
def on_add_button_click():
    product_name = entry_product_name.get()
    category = entry_category.get()
    price = entry_price.get()
    quantity = entry_quantity.get()

    # Проверяем, что все поля заполнены
    if not product_name or not category or not price or not quantity:
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Ошибка", "Цена должна быть числом, а количество целым числом!")
        return

    # Подключаемся к базе данных и добавляем продукт
    conn = connect_to_db()
    if conn:
        create_table(conn)
        add_product_to_db(product_name, category, price, quantity, conn)
        conn.close()

# Создаем главное окно
root = Tk()
root.title("Добавление продуктов")

# Создаем и размещаем элементы интерфейса
label_product_name = Label(root, text="Название продукта:")
label_product_name.grid(row=0, column=0, padx=10, pady=10)

entry_product_name = Entry(root)
entry_product_name.grid(row=0, column=1, padx=10, pady=10)

label_category = Label(root, text="Категория:")
label_category.grid(row=1, column=0, padx=10, pady=10)

entry_category = Entry(root)
entry_category.grid(row=1, column=1, padx=10, pady=10)

label_price = Label(root, text="Цена:")
label_price.grid(row=2, column=0, padx=10, pady=10)

entry_price = Entry(root)
entry_price.grid(row=2, column=1, padx=10, pady=10)

label_quantity = Label(root, text="Количество:")
label_quantity.grid(row=3, column=0, padx=10, pady=10)

entry_quantity = Entry(root)
entry_quantity.grid(row=3, column=1, padx=10, pady=10)

button_add = Button(root, text="Добавить", command=on_add_button_click)
button_add.grid(row=4, column=0, columnspan=2, pady=10)

# Запускаем основной цикл окна
root.mainloop()