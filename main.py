import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import os
from tkinter import Menu
import tkinter.messagebox as mb
from math import sqrt


class ShowInfoUser(object):
    def show_info_ver(self):
        msg = "Текущая версия приложения: 0.1.0"
        mb.showinfo("Версия", msg)

    def show_info_Pycharm(self):
        msg = "Pycharm ver 2022.3.2"
        mb.showinfo("Pycharm", msg)

    def show_info_PyQT(self):
        msg = "PyQT lib for python !pip install pyqt"
        mb.showinfo("Pyqt", msg)

    def show_info_Python(self):
        msg = "Python ver 3.11"
        mb.showinfo("Python", msg)

    def show_info_date(self):
        msg = "Создан: 12.02.2024"
        mb.showinfo("Дата создания", msg)


show_info = ShowInfoUser()


class Formulas:
    def discriminant(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = round((-b - discriminant ** 0.5) / (2 * a), 2)
            x2 = round((-b + discriminant ** 0.5) / (2 * a), 2)
            return x1, x2
        elif discriminant == 0:
            x = round(-b / (2 * a), 2)
            return x
        else:
            return "Комплексные корни"

    def difference_square(self, a, b):
        return (a - b) ** 2

    def fsy(self, a, b):
        return (a - b) * (a + b)

    def difference_cube(self, a, b):
        return (a - b) ** 3

    def summa_cube(self, a, b):
        return (a + b) ** 3


show_formulas = Formulas()
formulas_info = {
    "Квадратичная функция": "Введите 3 числа (a, b, c)",
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
        if formula == "Квадратичная функция" and len(numbers) == 3:
            result = show_formulas.discriminant(*numbers)
        elif formula == "Квадрат разности" and len(numbers) == 2:
            result = show_formulas.difference_square(*numbers)
        elif formula == "Разность квадратов" and len(numbers) == 2:
            result = show_formulas.fsy(*numbers)
        elif formula == "Разность кубов" and len(numbers) == 2:
            result = show_formulas.difference_cube(*numbers)
        elif formula == "Сумма кубов" and len(numbers) == 2:
            result = show_formulas.summa_cube(*numbers)
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

information_label = tk.Label(root, text='Введите 3 числа (a, b, c)', wraplength=200, font=("Arial", 12))
information_label.pack()

information_label_formulas = tk.Label(root, text='(ax ^ 2 + bx + c)', wraplength=200, font=("Arial", 12))
information_label_formulas.pack(pady=10)

input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack(pady=5)

calculate_button = tk.Button(root, command=calculate_formula, bd=0, text="Вычислить", **button_style, borderwidth=0)
calculate_button.place(relx=0.5, rely=0.7, anchor="center")
file_menu = Menu(tearoff=0)
file_menu.add_command(label="Квадратичная функция", command=lambda: option_variable.set("Квадратичная функция"))
file_menu.add_command(label="Квадрат разности", command=lambda: option_variable.set("Квадрат разности"))
file_menu.add_command(label="Разность квадратов", command=lambda: option_variable.set("Разность квадратов"))
file_menu.add_command(label="Разность кубов", command=lambda: option_variable.set("Разность кубов"))
file_menu.add_command(label="Сумма кубов", command=lambda: option_variable.set("Сумма кубов"))
file_menu.add_separator()

tools_menu = Menu(tearoff=0)
tools_menu.add_command(label="PyCharm", command=show_info.show_info_Pycharm)
tools_menu.add_command(label="PyQT", command=show_info.show_info_PyQT)
tools_menu.add_command(label="Python 3.11", command=show_info.show_info_Python)

version_menu = Menu(tearoff=0)
version_menu.add_command(label="Версия", command=show_info.show_info_ver)
version_menu.add_cascade(label="Инструменты", menu=tools_menu)
version_menu.add_separator()
version_menu.add_command(label="Дата создания", command=show_info.show_info_date)

main_menu = Menu(tearoff=0)
main_menu.add_cascade(label="Меню", menu=file_menu)
main_menu.add_cascade(label="Версия", menu=version_menu)
file_menu.add_command(label="Закрыть", command=root.destroy)
root.config(menu=main_menu)

root.mainloop()
