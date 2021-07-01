import tkinter as tk


class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Label Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("250x700")
        self.resizable(0, 0)
        self.config(bg="blue")

        self.create_widgets()

    def create_widgets(self):
        name_label_1 = tk.Label(self, text='Hello, my name is Mike.')
        name_label_1.pack()

        name_label_2 = tk.Label(
            self, text='Hello, my name is John.', font=('Arial', 18, 'bold'))
        name_label_2.pack()

        name_label_3 = tk.Label(
            self, text="Hello, my name is Paul", font=('Cambria', 10),
            bg="#ff0000")
        name_label_3.pack(padx=10, pady=50)

        name_label_4 = tk.Label(
            self, text='Hello, my name is Sue', bg="#000000", fg='green')
        name_label_4.pack(pady=(0, 10), ipadx=50, ipady=10, anchor='w')

        name_label_5 = tk.Label(
            self, text='Hello, my name is Pat', bg='#ffffff', fg="#123456")
        name_label_5.pack(fill="both", expand=True, padx=10, pady=10)


if __name__ == "__main__":
    app = Example()
    app.mainloop()
