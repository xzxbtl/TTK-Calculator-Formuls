

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys, os

def discriminant(a, x, b, c):
    return a * (x * x) + b * x + c


def difference_square(a, b):
    return (a - b) ** 2


def fsy(a, b):
    return (a - b) * (a + b)


def difference_cube(a, b):
    return (a - b) ** 3


def summa_cube(a, b):
    return (a + b) ** 3


formulas_info = {
    "Квадратичная функция": "Введите 4 числа (a, x, b, c)",
    "Квадрат разности": "Введите 2 числа (a, b)",
    "Разность квадратов": "Введите 2 числа (a, b)",
    "Разность кубов": "Введите 2 числа (a, b)",
    "Сумма кубов": "Введите 2 числа (a, b)"
}
formulas = {
    "Квадратичная функция": "(ax ^ 2 + bx + c)",
    "Квадрат разности": "(a - b) ^ 2",
    "Разность квадратов": "(a - b) * (a + b)",
    "Разность кубов": "(a - b) ^ 3",
    "Сумма кубов": "(a + b) ^ 3"
}


def show_formula_info(*args):
    selected_formula = option_variable.get()
    information_label.config(text=formulas_info[selected_formula])
    information_label_formulas.config(text=formulas[selected_formula])


def calculate_formula():
    formula = option_variable.get()
    numbers = input_entry.get().split()
    try:
        numbers = list(map(int, numbers))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")
        return

    try:
        if formula == "Квадратичная функция" and len(numbers) == 4:
            result = discriminant(*numbers)
        elif formula == "Квадрат разности" and len(numbers) == 2:
            result = difference_square(*numbers)
        elif formula == "Разность квадратов" and len(numbers) == 2:
            result = fsy(*numbers)
        elif formula == "Разность кубов" and len(numbers) == 2:
            result = difference_cube(*numbers)
        elif formula == "Сумма кубов" and len(numbers) == 2:
            result = summa_cube(*numbers)
        else:
            messagebox.showerror("Ошибка", "Неправильное количество чисел для выбранной формулы")
            return

        calculate_button.config(text="Результат: " + str(result))

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")


def show_output():
    output_window = tk.Toplevel(root)
    output_window.title("Результат")
    output_window.geometry("200x150")

    result_label = tk.Label(output_window, text="Здесь будет результат расчета", font=("Arial", 12))
    result_label.pack(pady=10)

image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sources")
icon_path = os.path.join(image_folder, "free-icon-calculator-buttons-interface-symbol-43148.png")
image_path = os.path.join(image_folder, "4238568.jpg")

root = tk.Tk()
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file=icon_path))
root.title("Calculator")
root.geometry("400x300")
root.resizable(False, False)

img = Image.open(image_path)
bg_image = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button_style = {"border": 0, "highlightthickness": 0, "activebackground": "#E0E0E0", "bg": "#4CAF50", "fg": "#FFFFFF",
                "font": ("Arial", 12), "highlightbackground": "#4CAF50"}
styled_button = {"border": 0, "highlightthickness": 0, "activebackground": "#E0E0E0", "relief": "flat", "bg": "#4CAF50",
                 "fg": "#FFFFFF", "font": ("Arial", 12), "highlightbackground": "#4CAF50"}
tk.TButton = lambda *args, **kwargs: tk.Button(*args, **kwargs, **styled_button)

formula_label = tk.Label(root, text="Выберите формулу:", font=("Arial", 12), compound='center')
formula_label.pack(pady=5)

formula_options = ["Квадратичная функция", "Квадрат разности", "Разность квадратов", "Разность кубов", "Сумма кубов"]

option_variable = tk.StringVar(root)
option_variable.set(formula_options[0])

formula_menu = tk.OptionMenu(root, option_variable, *formula_options)
formula_menu.config(font=("Arial", 12))
formula_menu.pack(pady=5)

option_variable.trace("w", show_formula_info)

information_label = tk.Label(root, text='Введите 4 числа (a, x, b, c)', wraplength=200, font=("Arial", 12))
information_label.pack()

information_label_formulas = tk.Label(root, text='(ax ^ 2 + bx + c)', wraplength=200, font=("Arial", 12))
information_label_formulas.pack(pady=10)

input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5)

calculate_button = tk.Button(root, command=calculate_formula, bd=0, text="Вычислить", **button_style, borderwidth=0)
calculate_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
