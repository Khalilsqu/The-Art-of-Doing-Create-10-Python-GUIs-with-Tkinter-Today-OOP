import tkinter as tk

class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Button Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("500x500")

        self.create_ui()

    def create_ui(self):
        # Define frames
        pack_frame = tk.Frame(self, bg='red')
        grid_frame_1 = tk.Frame(self, bg='blue')
        grid_frame_2 = tk.LabelFrame(
            self, text='Grid system rules!', borderwidth=5)

        # Pack frames onto self
        pack_frame.pack(fill="both", expand=True)
        grid_frame_1.pack(fill='x', expand=True)
        grid_frame_2.pack(fill="both", expand=True, padx=10, pady=10)

        # pack frame
        tk.Label(pack_frame, text='text').pack()
        tk.Label(pack_frame, text='text').pack()
        tk.Label(pack_frame, text='text').pack()

        # Grid 1 layout
        tk.Label(grid_frame_1, text='text').grid(row=0, column=0)
        tk.Label(grid_frame_1, text='text').grid(row=1, column=1)
        tk.Label(grid_frame_1, text='text').grid(row=2, column=2)
        #tk.Label(grid_frame_1, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=3, column=0)

        # Grid 2 layout
        tk.Label(grid_frame_2, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(
            row=0, column=0)


if __name__ == "__main__":
    app = Example()
    app.mainloop()
