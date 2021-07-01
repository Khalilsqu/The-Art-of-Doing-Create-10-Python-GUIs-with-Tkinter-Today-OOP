import tkinter as tk


class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Entry Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("500x500")
        self.resizable(0, 0)

        self.create_ui()

    def create_ui(self):
        input_frame = tk.Frame(self, bg='#0000ff', width=500, height=100)
        self.output_frame = tk.Frame(self, bg='#ff0000', width=500, height=400)
        input_frame.pack(padx=10, pady=10)
        self.output_frame.pack(padx=10, pady=(0, 10))

        # Add inputs
        self.text_entry = tk.Entry(input_frame, width=40)
        self.text_entry.grid(row=0, column=0, padx=5, pady=5)
        input_frame.grid_propagate(0)

        print_button = tk.Button(
            input_frame, text="Print!", command=self.make_label)
        print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

        # Keep output frame size
        self.output_frame.pack_propagate(0)

        # Pass a parameter with lambda
        self.value = 5
        count_button = tk.Button(
            input_frame, text="Count!",
            command=lambda: self.count_up(self.value))
        count_button.grid(row=1, column=0, columnspan=2,
                          padx=5, pady=5, sticky="WE")

    def make_label(self):
        '''Print a label to the app'''
        text = tk.Label(self.output_frame,
                        text=self.text_entry.get(), bg='#ff0000')
        text.pack()

        self.text_entry.delete(0, "end")

    def count_up(self, number):
        '''Count up on the app'''

        text = tk.Label(self.output_frame, text=number, bg="#ff0000")
        text.pack()

        self.value = number + 1


if __name__ == "__main__":
    app = Example()
    app.mainloop()
