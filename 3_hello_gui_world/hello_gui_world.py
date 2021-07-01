import tkinter as tk
from PIL import Image, ImageTk
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):

    root_color = "#224870"
    input_color = "#2a4494"
    output_color = "#4ea5d9"

    def __init__(self):
        super().__init__()
        self.title("Hello GUI World!")
        self.iconbitmap(absolute_base + '\wave.ico')
        self.geometry("400x400")
        self.resizable(0, 0)
        self.config(bg=self.root_color)

        self.create_ui()

    def create_ui(self):
        input_frame = tk.LabelFrame(self, bg=self.input_color)
        self.output_frame = tk.LabelFrame(self, bg=self.output_color)
        input_frame.pack(pady=10)
        self.output_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        self.name = tk.Entry(input_frame, text="Enter your name", width=20)
        submit_button = tk.Button(
            input_frame, text="Submit", command=self.submit_name)
        self.name.grid(row=0, column=0, padx=10, pady=10)
        submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

        self.case_style = tk.StringVar(value="normal")
        normal_button = tk.Radiobutton(
            input_frame, text="Normal Case", variable=self.case_style,
            value='normal', bg=self.input_color)
        upper_button = tk.Radiobutton(
            input_frame, text="Upper Case", variable=self.case_style,
            value='upper', bg=self.input_color)
        normal_button.grid(row=1, column=0, padx=2, pady=2)
        upper_button.grid(row=1, column=1, padx=2, pady=2)

        # Add an image
        self.smile_img = ImageTk.PhotoImage(
            Image.open(absolute_base + "\smile.png"))
        smile_label = tk.Label(
            self.output_frame, image=self.smile_img, bg=self.output_color)
        smile_label.pack()

    def submit_name(self):
        """Say hello to the user."""
        # Create a label for the user name based of radio button values
        if self.case_style.get() == 'normal':
            name_label = tk.Label(self.output_frame, text="Hello " +
                                  self.name.get() + "! Keep learning Tkinter!",
                                  bg=self.output_color)
        elif self.case_style.get() == 'upper':
            name_label = tk.Label(self.output_frame, text=(
                "Hello " + self.name.get() + "! Keep learning Tkinter!").upper(),
                bg=self.output_color)

        name_label.pack()

        # Clear the entry field for the next user
        self.name.delete(0, "end")


if __name__ == "__main__":
    app = Example()
    app.mainloop()
