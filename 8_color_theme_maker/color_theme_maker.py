import tkinter as tk
from tkinter import filedialog
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Color Theme Maker')
        self.iconbitmap(absolute_base + '/color_wheel.ico')
        self.geometry('450x500')
        self.resizable(0, 0)

        self.setup_ui()

    def setup_ui(self):
        # Define Layout

        self.input_frame = tk.LabelFrame(self, padx=5, pady=5)
        self.output_frame = tk.LabelFrame(self, padx=5, pady=5)
        self.input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Setting up the input frame.
        # Create the labels, sliders, and buttons for each color RGB
        red_label = tk.Label(self.input_frame, text="R")
        self.red_slider = tk.Scale(
            self.input_frame, from_=0, to=255, command=self.get_red)
        red_button = tk.Button(
            self.input_frame, text="Red", command=lambda: self.set_color(255, 0, 0))
        green_label = tk.Label(self.input_frame, text="G")
        self.green_slider = tk.Scale(
            self.input_frame, from_=0, to=255, command=self.get_green)
        green_button = tk.Button(
            self.input_frame, text="Green", command=lambda: self.set_color(0, 255, 0))
        blue_label = tk.Label(self.input_frame, text="B")
        self.blue_slider = tk.Scale(
            self.input_frame, from_=0, to=255, command=self.get_blue)
        blue_button = tk.Button(
            self.input_frame, text="Blue", command=lambda: self.set_color(0, 0, 255))

        # Create buttons for each complimentary color
        yellow_button = tk.Button(
            self.input_frame, text="Yellow", command=lambda: self.set_color(255, 255, 0))
        cyan_button = tk.Button(
            self.input_frame, text="Cyan", command=lambda: self.set_color(0, 255, 255))
        magenta_button = tk.Button(
            self.input_frame, text="Magenta", command=lambda: self.set_color(255, 0, 255))

        # Create utility buttons
        store_button = tk.Button(
            self.input_frame, text="Store Color", command=self.store_color)
        save_button = tk.Button(
            self.input_frame, text="Save", command=self.save_colors)
        quit_button = tk.Button(
            self.input_frame, text="Quit", command=self.destroy)

        # Put labels, sliders, and buttons on to the frame....Use ipadx with
        # rbg buttons to define column width, then use sticky on others
        red_label.grid(row=0, column=0, sticky='W')
        self.red_slider.grid(row=1, column=0, sticky='W')
        red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)
        green_label.grid(row=0, column=1, sticky='W')
        self.green_slider.grid(row=1, column=1, sticky='W')
        green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=15)
        blue_label.grid(row=0, column=2, sticky='W')
        self.blue_slider.grid(row=1, column=2, sticky='W')
        blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=18)
        yellow_button.grid(row=3, column=0, padx=1, pady=1, sticky="WE")
        cyan_button.grid(row=3, column=1, padx=1, pady=1, sticky="WE")
        magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky="WE")
        store_button.grid(row=4, column=0, columnspan=3,
                          padx=1, pady=1, sticky="WE")
        save_button.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
        quit_button.grid(row=4, column=4, padx=1, pady=1, sticky="WE")

        # Create the color box and color labels
        color_box = tk.Label(self.input_frame, bg='black', height=6, width=15)
        self.color_tuple = tk.Label(self.input_frame, text='(0), (0), (0)')
        self.color_hex = tk.Label(self.input_frame, text='#000000')

        # Put the color box and labels on the frame.
        color_box.grid(row=1, column=3, columnspan=2,
                       padx=35, pady=10, ipadx=10, ipady=10)
        self.color_tuple.grid(row=2, column=3, columnspan=2)
        self.color_hex.grid(row=3, column=3, columnspan=2)

        # Setting up the output frame
        # Initialize a dictionary to hold all stored colors
        self.stored_colors = {}
        self.stored_color = tk.IntVar()

        # Create radio buttons to select stored colors and populate each row
        # with placeholder values
        for i in range(6):
            radio = tk.Radiobutton(
                self.output_frame, variable=self.stored_color, value=i)
            radio.grid(row=i, column=0, sticky='W')

            recall_button = tk.Button(
                self.output_frame, text="Recall Color", state=tk.DISABLED)
            new_color_tuple = tk.Label(
                self.output_frame, text="(255), (255), (255)")
            new_color_hex = tk.Label(self.output_frame, text="#ffffff")
            new_color_black_box = tk.Label(
                self.output_frame, bg="black", width=3, height=1)
            new_color_box = tk.Label(
                self.output_frame, bg='white', width=3, height=1)

            recall_button.grid(row=i, column=1, padx=20)
            new_color_tuple.grid(row=i, column=2, padx=20)
            new_color_hex.grid(row=i, column=3, padx=20)
            new_color_black_box.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
            new_color_box.grid(row=i, column=4)

            # .cget() returns the value of a specific option.  Store the text
            # value of the tuple label and hex label
            self.stored_colors[self.stored_color.get()] = \
                [new_color_tuple.cget(
                    'text'), new_color_hex.cget('text')]

        # Initialize the starting values for the color box display
        self.red_value = "00"
        self.green_value = "00"
        self.blue_value = "00"

    # Define methods

    def get_red(self, slider_value):
        """
        Turn current slider value for red into a hex value and update color.
        The scale value is passed automatically when the scale is moved 
        calling the get_red function.
        """

        # Turn the slider value into an int and hex value. Strip leading chars
        # so only two remain
        self.red_value = hex(int(slider_value))
        self.red_value = self.red_value.lstrip("0x")

        # If hex value is single digit, lead with a 0 such that d becomes 0d
        while len(self.red_value) < 2:
            self.red_value = "0" + str(self.red_value)

        self.update_color()

    def get_green(self, slider_value):
        """
        Turn current slider value for green into a hex value and update color.
        The scale value is passed automatically when the scale is moved 
        calling the get_green function.
        """

        # Turn the slider value into an int and hex value. Strip leading
        # chars so only two remain
        self.green_value = hex(int(slider_value))
        self.green_value = self.green_value.lstrip("0x")

        # If hex value is single digit, lead with a 0 such that d becomes 0d
        while len(self.green_value) < 2:
            self.green_value = "0" + str(self.green_value)

        self.update_color()

    def get_blue(self, slider_value):
        """
        Turn current slider value for blue into a hex value and update color.
        The scale value is passed automatically when the scale is moved 
        calling the get_blue function.
        """

        # Turn the slider value into an int and hex value. Strip leading
        # chars so only two remain
        self.blue_value = hex(int(slider_value))
        self.blue_value = self.blue_value.lstrip("0x")

        # If hex value is single digit, lead with a 0 such that d becomes 0d
        while len(self.blue_value) < 2:
            self.blue_value = "0" + str(self.blue_value)

        self.update_color()

    def update_color(self):
        """
        UPdate the current color box based on the slider values.  
        Display tuple and hex values of the current color
        """
        # Make the color box smaller than the original due to ipadx and ipday
        # on the original color box
        color_box = tk.Label(self.input_frame, bg="#" + self.red_value +
                             self.green_value + self.blue_value, height=6,
                             width=15)
        color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10)

        # Display the tuple and hex value for the given color
        self.color_tuple.config(
            text='(' + str(self.red_slider.get()) + '),' + '(' +
            str(self.green_slider.get()) + '),' +
            '(' + str(self.blue_slider.get()) + ')')
        self.color_hex.config(text="#" + self.red_value +
                              self.green_value + self.blue_value)

    def set_color(self, r, g, b):
        """Set a given color"""
        self.red_slider.set(r)
        self.green_slider.set(g)
        self.blue_slider.set(b)

    def store_color(self):
        """Store the current color tuple value and display color"""

        # Get the current value of each slider and append 0's to keep
        # formatting
        red = str(self.red_slider.get())
        while len(red) < 3:
            red = "0" + red

        green = str(self.green_slider.get())
        while len(green) < 3:
            green = "0" + green

        blue = str(self.blue_slider.get())
        while len(blue) < 3:
            blue = "0" + blue

        # Keep a reference of the current color
        stored_red = self.red_slider.get()
        stored_green = self.green_slider.get()
        stored_blue = self.blue_slider.get()

        # Create new widgets for the stored color.
        recall_button = tk.Button(
            self.output_frame, text="Recall Color",
            command=lambda: self.set_color(
                stored_red, stored_green, stored_blue)
        )
        new_color_tuple = tk.Label(
            self.output_frame, text='(' + red + '),' + '(' + green + '),'
            + '(' + blue + ')')
        new_color_hex = tk.Label(self.output_frame, text='#' +
                                 self.red_value + self.green_value +
                                 self.blue_value)
        new_color_black_box = tk.Label(
            self.output_frame, bg='black', width=3, height=1)
        new_color_box = tk.Label(self.output_frame, bg="#" + self.red_value +
                                 self.green_value + self.blue_value, width=3,
                                 height=1)

        # Put new widgets on the screen
        recall_button.grid(row=self.stored_color.get(), column=1, padx=20)
        new_color_tuple.grid(row=self.stored_color.get(), column=2, padx=20)
        new_color_hex.grid(row=self.stored_color.get(), column=3, padx=20)
        new_color_black_box.grid(row=self.stored_color.get(),
                                 column=4, pady=2, ipadx=5, ipady=5)
        new_color_box.grid(row=self.stored_color.get(), column=4)

        # Update the dict stored_colors with the new color tuple and hex values
        self.stored_colors[self.stored_color.get()] = [new_color_tuple.cget(
            "text"), new_color_hex.cget("text")]

        # Move the radio button stored colors_ to the next value if available
        if self.stored_color.get() < 5:
            self.stored_color.set(self.stored_color.get() + 1)

    def save_colors(self):
        """Output the chosen colors to a txt file."""
        # Get the directory where the user would like to save
        file_name = filedialog.asksaveasfilename(
            initialdir='./', title='Save Colors',
            filetypes=(('Text', '.txt'),
                       ('All Files', '*.*')))

        # open the new file as write
        if file_name:
            with open(file_name, "w") as f:
                f.write("Color Theme Maker Output\n")
                for saved_entry in self.stored_colors.values():
                    f.write(saved_entry[0] + "\n" + saved_entry[1] + "\n\n")


if __name__ == "__main__":
    app = Example()
    app.mainloop()
