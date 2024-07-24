import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

def plot_bessel_functions(order):
    x = np.linspace(-30, 30, 600)
    fig, ax = plt.subplots()
    y = jn(order, x)
    ax.plot(x, y, label=f"J_({order})(x)", color='green')
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_title("Функции Бесселя I рода")
    ax.set_xlabel("x")
    ax.set_ylabel("J_n(x)")
    ax.legend()
    return fig

def plot_3d_bessel_functions(min_order, max_order):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, 20, 600)
    y = np.linspace(min_order, max_order, 600)
    X, Y = np.meshgrid(x, y)
    Z = jn(Y, X)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel("x")
    ax.set_ylabel("порядок")
    ax.set_zlabel("J_n(x)")
    return fig

class Bessel:
    def __init__(self, root):
        self.root = root
        self.root.title("Построение графиков функций Бесселя I рода")

        self.tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='2D')
        self.tab_control.add(self.tab2, text='3D')
        self.tab_control.pack(expand=1, fill='both')

        self.figure_canvas_2d = None
        self.figure_canvas_3d = None

        self.plot_2d()
        self.plot_3d()

    def plot_2d(self):
        order_label = tk.Label(self.tab1, text="Введите порядок")
        order_label.pack()
        self.order_entry = tk.Entry(self.tab1)
        self.order_entry.pack()

        self.plot_button_2d = tk.Button(self.tab1, text="Ввести", command=self.plot_2d_callback)
        self.plot_button_2d.pack()

    def plot_2d_callback(self):
        order = float(self.order_entry.get())
        fig_2d = plot_bessel_functions(order)

        if self.figure_canvas_2d:
            self.figure_canvas_2d.get_tk_widget().pack_forget()
        self.figure_canvas_2d = FigureCanvasTkAgg(fig_2d, master=self.tab1)
        self.figure_canvas_2d.get_tk_widget().pack()

    def plot_3d(self):
        min_order_label = tk.Label(self.tab2, text="Введите нижнюю границу порядка")
        min_order_label.pack()
        self.min_order_entry = tk.Entry(self.tab2)
        self.min_order_entry.pack()

        max_order_label = tk.Label(self.tab2, text="Введите верхнюю границу порядка")
        max_order_label.pack()
        self.max_order_entry = tk.Entry(self.tab2)
        self.max_order_entry.pack()

        self.plot_button_3d = tk.Button(self.tab2, text="Ввести", command=self.plot_3d_callback)
        self.plot_button_3d.pack()

    def plot_3d_callback(self):
        min_order = float(self.min_order_entry.get())
        max_order = float(self.max_order_entry.get())
        fig_3d = plot_3d_bessel_functions(min_order, max_order)

        if self.figure_canvas_3d:
            self.figure_canvas_3d.get_tk_widget().pack_forget()
        self.figure_canvas_3d = FigureCanvasTkAgg(fig_3d, master=self.tab2)
        self.figure_canvas_3d.get_tk_widget().pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = Bessel(root)
    root.mainloop()
