import tkinter as tk


class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Radio Button Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("350x350")
        self.resizable(0, 0)

        self.create_ui()

    def create_ui(self):
        input_frame = tk.LabelFrame(
            self, text='This is fun!', width=350, height=100)
        self.output_frame = tk.Frame(self, width=350, height=250)
        input_frame.pack(padx=10, pady=10)
        self.output_frame.pack(padx=10, pady=(0, 10))

        self.number = tk.IntVar(value=1)
        radio_1 = tk.Radiobutton(
            input_frame, text='Print the number one!',
            variable=self.number, value=1)
        radio_2 = tk.Radiobutton(
            input_frame, text="Print the number two!",
            variable=self.number, value=2)
        print_button = tk.Button(
            input_frame, text="Print the number!", command=self.make_label)

        radio_1.grid(row=0, column=0, padx=10, pady=10)
        radio_2.grid(row=0, column=1, padx=10, pady=10)
        print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def make_label(self):
        '''Print to the screen'''
        if self.number.get() == 1:
            num_label = tk.Label(self.output_frame, text="1 one 1")
        elif self.number.get() == 2:
            num_label = tk.Label(self.output_frame, text="2 two 2")

        num_label.pack()


if __name__ == "__main__":
    app = Example()
    app.mainloop()
