import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showwarning("Увага", "Пароль має бути хоча б з 1 символа.")
            return
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть ціле число.")
        return

    char_pool = ''
    if var_lower.get():
        char_pool += string.ascii_lowercase
    if var_upper.get():
        char_pool += string.ascii_uppercase
    if var_digits.get():
        char_pool += string.digits
    if var_symbols.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showwarning("Увага", "Оберіть хоча б один тип символів.")
        return

    password = ''.join(random.choices(char_pool, k=length))
    result_var.set(password)

# Вікно
window = tk.Tk()
window.title("Генератор паролів")
window.geometry("420x300")
window.resizable(False, False)

# Заголовок
tk.Label(window, text="Генератор надійних паролів", font=("Arial", 14, "bold")).pack(pady=10)

# Довжина
length_frame = tk.Frame(window)
length_frame.pack()
tk.Label(length_frame, text="Довжина пароля:").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT)

# Чекбокси
options_frame = tk.Frame(window)
options_frame.pack(pady=10)

var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Малі літери (a-z)", variable=var_lower).grid(row=0, column=0, sticky='w')
tk.Checkbutton(options_frame, text="Великі літери (A-Z)", variable=var_upper).grid(row=1, column=0, sticky='w')
tk.Checkbutton(options_frame, text="Цифри (0-9)", variable=var_digits).grid(row=0, column=1, sticky='w')
tk.Checkbutton(options_frame, text="Символи (!@#$...)", variable=var_symbols).grid(row=1, column=1, sticky='w')

# Кнопка генерації
tk.Button(window, text="Згенерувати пароль", command=generate_password).pack(pady=10)

# Результат
result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, font=("Courier", 12), justify='center', state='readonly', width=35).pack(pady=5)

# Старт
window.mainloop()
