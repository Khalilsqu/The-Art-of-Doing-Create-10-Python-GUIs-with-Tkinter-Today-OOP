import tkinter as tk


class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Window Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("250x700")
        self.resizable(0, 0)
        self.config(bg="blue")

        self.second_window()

    def second_window(self):
        top = tk.Toplevel()

        top.title("Second window")
        top.config(bg="#123456")
        top.geometry("200x200+500+50")


if __name__ == "__main__":
    app = Example()
    app.mainloop()
