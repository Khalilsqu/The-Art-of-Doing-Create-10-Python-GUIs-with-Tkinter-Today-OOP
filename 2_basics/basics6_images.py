import tkinter as tk
from PIL import Image, ImageTk

class Example(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Image Basics!")
        self.iconbitmap('thinking.ico')
        self.geometry("700x700")

        self.create_ui()

    def create_ui(self):
        self.my_image = tk.PhotoImage(file="shield.png")
        my_label = tk.Label(self, image=self.my_image)
        my_label.pack()

        my_button = tk.Button(self, image=self.my_image)
        my_button.pack()

        self.make_image()

    def make_image(self):
        cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
        cat_label = tk.Label(self, image=cat_image)
        cat_image.image = cat_image
        cat_label.pack()

if __name__ == "__main__":
    app = Example()
    app.mainloop()
