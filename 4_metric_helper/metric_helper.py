import tkinter as tk
from PIL import Image, ImageTk
from os import path
from tkinter.ttk import Combobox

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):

    field_font = ('Cambria', 10)
    bg_color = "#c75c5c"
    button_color = "#f5cf87"

    metric_values = {
        'femto': 10**-15,
        'pico': 10**-12,
        'nano': 10**-9,
        'micro': 10**-6,
        'milli': 10**-3,
        'centi': 10**-2,
        'deci': 10**-1,
        'base value': 10**0,
        'deca': 10**1,
        'hecto': 10**2,
        'kilo': 10**3,
        'mega': 10**6,
        'giga': 10**9,
        'tera': 10**12,
        'peta': 10**15
    }

    def __init__(self):
        super().__init__()
        self.title("Hello GUI World!")
        self.iconbitmap(absolute_base + '/ruler.ico')
        self.geometry("400x400")
        self.resizable(0, 0)
        self.config(bg=Example.bg_color)

        self.create_ui()

    def create_ui(self):
        self.input_field = tk.Entry(
            self, width=20, font=Example.field_font, borderwidth=3)
        self.output_field = tk.Entry(
            self, width=20, font=Example.field_font, borderwidth=3)
        equal_label = tk.Label(
            self, text="=", font=Example.field_font, bg=Example.bg_color)

        self.input_field.grid(row=0, column=0, padx=10, pady=10)
        equal_label.grid(row=0, column=1, padx=10, pady=10)
        self.output_field.grid(row=0, column=2, padx=10, pady=10)

        self.input_field.insert(0, 'Enter your quantity')

        metric_list = ['femto', 'pico', 'nano', 'micro', 'milli', 'centi',
                       'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega',
                       'giga', 'tera', 'peta']
        self.input_combobox = Combobox(
            self, value=metric_list, font=Example.field_font, justify='center')
        self.output_combobox = Combobox(
            self, value=metric_list, font=Example.field_font, justify='center')
        to_label = tk.Label(
            self, text="to", font=Example.field_font, bg=Example.bg_color)

        self.input_combobox.grid(row=1, column=0, padx=10, pady=10)
        to_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_combobox.grid(row=1, column=2, padx=10, pady=10)

        self.input_combobox.set('base value')
        self.output_combobox.set('base value')

        # Create a conversion button
        convert_button = tk.Button(
            self, text='Convert', font=Example.field_font,
            bg=Example.button_color, command=self.convert)
        convert_button.grid(row=2, column=0, columnspan=3,
                            padx=10, pady=10, ipadx=50)

    def convert(self):
        """Convert from one metric prefix to another"""

        # Clear the output field
        self.output_field.delete(0, tk.END)

        # Get all user information
        start_value = float(self.input_field.get())
        start_prefix = self.input_combobox.get()
        end_prefix = self.output_combobox.get()

        # Covert to the base unit first
        base_value = start_value*self.metric_values[start_prefix]
        # Covert to new metric value
        end_value = base_value/self.metric_values[end_prefix]

        # Update ouput field with answer
        self.output_field.insert(0, str(end_value))


if __name__ == "__main__":
    app = Example()
    app.mainloop()
