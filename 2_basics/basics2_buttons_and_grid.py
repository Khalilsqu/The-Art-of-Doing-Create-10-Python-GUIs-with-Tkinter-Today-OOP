import tkinter as tk


class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Button Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("500x500")
        self.resizable(0, 0)

        self.create_ui()

    def create_ui(self):
        name_button = tk.Button(self, text="Name")
        name_button.grid(row=0, column=0)

        time_button = tk.Button(self, text="Time", bg="#00ffff")
        time_button.grid(row=0, column=1)

        place_button = tk.Button(self, text="Place", bg="#00ffff",
                                 activebackground="#ff0000")
        place_button.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

        day_button = tk.Button(self, text="Day")
        day_button = tk.Button(
            self, text="Day", bg='black', fg='white', borderwidth=5)
        day_button.grid(row=1, column=0, columnspan=3, sticky="WE")

        test_1 = tk.Button(self, text="test")
        test_2 = tk.Button(self, text="test")
        test_3 = tk.Button(self, text="test")
        test_4 = tk.Button(self, text="test")
        test_5 = tk.Button(self, text="test")
        test_6 = tk.Button(self, text="test")

        test_1.grid(row=2, column=0, padx=5, pady=5)
        test_2.grid(row=2, column=1, padx=5, pady=5)
        test_3.grid(row=2, column=2, padx=5, pady=5, sticky='W')
        test_4.grid(row=3, column=0, padx=5, pady=5)
        test_5.grid(row=3, column=1, padx=5, pady=5)
        test_6.grid(row=3, column=2, padx=5, pady=5, sticky='W')


if __name__ == "__main__":
    app = Example()
    app.mainloop()
