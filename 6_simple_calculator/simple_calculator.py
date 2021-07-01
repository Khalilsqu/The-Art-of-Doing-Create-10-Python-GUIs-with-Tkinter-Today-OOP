import tkinter as tk
from tkinter import messagebox
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):
    # Define colors and fonts
    dark_green = '#93af22'
    light_green = '#acc253'
    white_green = '#edefe0'
    button_font = ('Arial', 18)
    display_font = ('Arial', 30)

    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.iconbitmap(absolute_base + '/calc.ico')
        self.geometry('300x400')
        self.resizable(0, 0)
        self.first_number = None

        self.define_layout()

    def define_layout(self):
        # GUI Layout
        # Define frames
        display_frame = tk.LabelFrame(self)
        button_frame = tk.LabelFrame(self)
        display_frame.pack(padx=2, pady=(5, 20))
        button_frame.pack(padx=2, pady=5)

        # Layout for the display frame
        self.display = tk.Entry(display_frame, width=50,
                                font=self.display_font, bg=self.white_green,
                                borderwidth=5, justify="right")
        self.display.pack(padx=5, pady=5)

        # Layout for the button frame
        clear_button = tk.Button(
            button_frame, text="Clear", font=self.button_font,
            bg=self.dark_green, command=self.clear)
        quit_button = tk.Button(
            button_frame, text="Quit", font=self.button_font,
            bg=self.dark_green, command=self.destroy)

        self.inverse_button = tk.Button(
            button_frame, text='1/x', font=self.button_font,
            bg=self.light_green, command=self.inverse)
        self.square_button = tk.Button(
            button_frame, text='x^2', font=self.button_font,
            bg=self.light_green, command=self.square)
        self.exponent_button = tk.Button(
            button_frame, text='x^n', font=self.button_font,
            bg=self.light_green, command=lambda: self.operate('exponent'))
        self.divide_button = tk.Button(
            button_frame, text=' / ', font=self.button_font,
            bg=self.light_green, command=lambda: self.operate('divide'))
        self.multiply_button = tk.Button(
            button_frame, text='*', font=self.button_font, bg=self.light_green,
            command=lambda: self.operate('multiply'))
        self.subtract_button = tk.Button(
            button_frame, text='-', font=self.button_font, bg=self.light_green,
            command=lambda: self.operate('subtract'))
        self.add_button = tk.Button(
            button_frame, text='+', font=self.button_font, bg=self.light_green,
            command=lambda: self.operate('add'))
        equal_button = tk.Button(
            button_frame, text='=', font=self.button_font, bg=self.dark_green,
            command=self.equal)
        self.decimal_button = tk.Button(
            button_frame, text='.', font=self.button_font, bg='black',
            fg='white', command=lambda: self.submit_number("."))
        negate_button = tk.Button(
            button_frame, text='+/-', font=self.button_font, bg='black',
            fg='white', command=self.negate)

        nine_button = tk.Button(button_frame, text='9', font=self.button_font,
                                bg='black', fg='white',
                                command=lambda: self.submit_number(9))
        eight_button = tk.Button(
            button_frame, text='8', font=self.button_font, bg='black',
            fg='white',
            command=lambda: self.submit_number(8))
        seven_button = tk.Button(
            button_frame, text='7', font=self.button_font, bg='black',
            fg='white',
            command=lambda: self.submit_number(7))
        six_button = tk.Button(button_frame, text='6', font=self.button_font,
                               bg='black', fg='white',
                               command=lambda: self.submit_number(6))
        five_button = tk.Button(button_frame, text='5', font=self.button_font,
                                bg='black', fg='white',
                                command=lambda: self.submit_number(5))
        four_button = tk.Button(button_frame, text='4', font=self.button_font,
                                bg='black', fg='white',
                                command=lambda: self.submit_number(4))
        three_button = tk.Button(
            button_frame, text='3', font=self.button_font, bg='black',
            fg='white', command=lambda: self.submit_number(3))
        two_button = tk.Button(button_frame, text='2', font=self.button_font,
                               bg='black', fg='white',
                               command=lambda: self.submit_number(2))
        one_button = tk.Button(button_frame, text='1', font=self.button_font,
                               bg='black', fg='white',
                               command=lambda: self.submit_number(1))
        zero_button = tk.Button(button_frame, text='0', font=self.button_font,
                                bg='black', fg='white',
                                command=lambda: self.submit_number(0))

        # First row
        clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky="WE")
        quit_button.grid(row=0, column=2, columnspan=2, pady=1, sticky="WE")
        # Second row
        self.inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
        self.square_button.grid(row=1, column=1, pady=1, sticky="WE")
        self.exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
        self.divide_button.grid(row=1, column=3, pady=1, sticky="WE")
        # Third row (Add padding to create the size of the columns)
        seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20)
        eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20)
        nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20)
        self.multiply_button.grid(
            row=2, column=3, pady=1, sticky="WE", ipadx=20)
        # Fourth row
        four_button.grid(row=3, column=0, pady=1, sticky="WE")
        five_button.grid(row=3, column=1, pady=1, sticky="WE")
        six_button.grid(row=3, column=2, pady=1, sticky="WE")
        self.subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
        # Fifth row
        one_button.grid(row=4, column=0, pady=1, sticky="WE")
        two_button.grid(row=4, column=1, pady=1, sticky="WE")
        three_button.grid(row=4, column=2, pady=1, sticky="WE")
        self.add_button.grid(row=4, column=3, pady=1, sticky="WE")
        # Sixth row
        negate_button.grid(row=5, column=0, pady=1, sticky="WE")
        zero_button.grid(row=5, column=1, pady=1, sticky="WE")
        self.decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
        equal_button.grid(row=5, column=3, pady=1, sticky="WE")

    def submit_number(self, number):
        """Add a number or decimal to the display"""
        # Insert the number or decimal pressed to the end of the display
        self.display.insert(tk.END, number)

        # If decimal was pressed, disable the decimal button so
        # it cannot be pressed twice
        if "." in self.display.get():
            self.decimal_button.config(state=tk.DISABLED)

    def operate(self, operator):
        """
        Store the first number of the expression and the operation to be used
        """
        if self.display.get():
            self.operation = operator
            self.first_number = self.display.get()

            # Delete the value (first number) from entry display
            self.display.delete(0, tk.END)

            # Dispable all operator buttons until equal or clear is pressed
            self.add_button.config(state=tk.DISABLED)
            self.subtract_button.config(state=tk.DISABLED)
            self.multiply_button.config(state=tk.DISABLED)
            self.divide_button.config(state=tk.DISABLED)
            self.exponent_button.config(state=tk.DISABLED)
            self.inverse_button.config(state=tk.DISABLED)
            self.square_button.config(state=tk.DISABLED)

            # Return decimal button to normal state
            self.decimal_button.config(state=tk.NORMAL)

    def equal(self):
        """Run the stored operation for two number."""
        # Perform the desired mathematics
        if self.display.get() and self.first_number:
            try:
                if self.operation == 'add':
                    value = eval(self.first_number) + eval(self.display.get())
                elif self.operation == 'subtract':
                    value = eval(self.first_number) - eval(self.display.get())
                elif self.operation == 'multiply':
                    value = eval(self.first_number) * eval(self.display.get())
                elif self.operation == 'divide':
                    if self.display.get() == "0":
                        value = "ERROR"
                    else:
                        value = eval(self.first_number) / \
                            eval(self.display.get())
                elif self.operation == 'exponent':
                    value = eval(self.first_number) ** eval(self.display.get())

                # Remove the curent value of the display and update it with the answer
                self.display.delete(0, tk.END)
                self.display.insert(0, value)

                # Return buttons to normal states
                self.enable_buttons()
                self.first_number = None
            except:
                x = self.winfo_x()
                y = self.winfo_y()
                w = self.winfo_width()//2
                h = self.winfo_height()//2
                top = tk.Toplevel(self)
                top.geometry(f"200x20+{w+x}+{h+y}")
                top.grab_set()
                top.wm_overrideredirect(True)
                label = tk.Label(top, text="Please enter none string values")
                label.config(bg="red", fg="black")
                label.pack(fill="both")
                self.after(2000, top.destroy)
                self.clear()

    def enable_buttons(self):
        """Enabel all butonns on the calculator"""
        self.decimal_button.config(state=tk.NORMAL)
        self.add_button.config(state=tk.NORMAL)
        self.subtract_button.config(state=tk.NORMAL)
        self.multiply_button.config(state=tk.NORMAL)
        self.divide_button.config(state=tk.NORMAL)
        self.exponent_button.config(state=tk.NORMAL)
        self.inverse_button.config(state=tk.NORMAL)
        self.square_button.config(state=tk.NORMAL)

    def clear(self):
        """Clear the display"""
        self.display.delete(0, tk.END)

        # Return buttons to normal state
        self.enable_buttons()

    def inverse(self):
        """Calculate the inverse of a given number."""
        # Do not allow for 1/0
        if self.display.get() == '0':
            value = 'ERROR'
        else:
            value = 1/float(self.display.get())

        # Remove the current value in the display and update it with the answer
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

    def square(self):
        """Calculate the square of a given number."""
        value = float(self.display.get())**2

        # Remove the current value in the display and update it with the answer
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

    def negate(self):
        """Negate a given number."""
        text = self.display.get()
        if text:
            try:
                value = -1*eval(self.display.get())

                # Remove the current value in the display and update it with the answer
                self.display.delete(0, tk.END)
                self.display.insert(0, value)
            except:
                pass


if __name__ == "__main__":
    app = Example()
    app.mainloop()
