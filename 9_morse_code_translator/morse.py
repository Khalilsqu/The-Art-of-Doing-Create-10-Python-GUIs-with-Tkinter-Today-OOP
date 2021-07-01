import tkinter as tk
from tkinter import IntVar, END, DISABLED, NORMAL
from winsound import PlaySound, SND_FILENAME
from PIL import ImageTk, Image
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):
    button_font = ('SimSun', 10)
    root_color = "#778899"
    frame_color = "#dcdcdc"
    button_color = "#c0c0c0"
    text_color = "#f8f8ff"

    english_to_morse = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7':  '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': ' ', '|': '|', "": ""
    }

    def __init__(self):
        super().__init__()
        self.title('Morse Code Translator')
        self.iconbitmap(absolute_base + '/morse.ico')
        self.geometry('500x350')
        self.resizable(0, 0)

        # self.config(bd=self.root_color)
        self.setup_ui()

    def setup_ui(self):
        self.morse_to_english = dict([(value, key) for key, value in
                                      self.english_to_morse.items()])

        # Define layout
        # Create frames
        input_frame = tk.LabelFrame(self, bg=self.frame_color)
        output_frame = tk.LabelFrame(self, bg=self.frame_color)
        input_frame.pack(padx=16, pady=(16, 8))
        output_frame.pack(padx=16, pady=(8, 16))

        # Layout for the input frame
        self.input_text = tk.Text(
            input_frame, height=8, width=30, bg=self.text_color)
        self.input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

        self.language = IntVar()
        self.language.set(1)
        morse_button = tk.Radiobutton(
            input_frame, text="English --> Morse Code", variable=self.language,
            value=1, font=self.button_font, bg=self.frame_color)
        english_button = tk.Radiobutton(
            input_frame, text="Morse Code --> English", variable=self.language,
            value=2, font=self.button_font, bg=self.frame_color)
        self.guide_button = tk.Button(
            input_frame, text="Guide", font=self.button_font,
            bg=self.button_color,
            command=self.show_guide)

        morse_button.grid(row=0, column=0, pady=(15, 0))
        english_button.grid(row=1, column=0)
        self.guide_button.grid(row=2, column=0, sticky="WE", padx=10)

        # Layout for the output frame
        self.output_text = tk.Text(
            output_frame, height=8, width=30, bg=self.text_color)
        self.output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

        convert_button = tk.Button(
            output_frame, text="Convert", font=self.button_font,
            bg=self.button_color,
            command=self.convert)
        play_button = tk.Button(
            output_frame, text="Play Morse", font=self.button_font,
            bg=self.button_color,
            command=self.play)
        clear_button = tk.Button(
            output_frame, text="Clear", font=self.button_font,
            bg=self.button_color,
            command=self.clear)
        quit_button = tk.Button(
            output_frame, text="Quit", font=self.button_font,
            bg=self.button_color,
            command=self.destroy)
        # convert ipadx defines column width
        convert_button.grid(row=0, column=0, padx=10, ipadx=50)
        play_button.grid(row=1, column=0, padx=10, sticky="WE")
        clear_button.grid(row=2, column=0, padx=10, sticky="WE")
        quit_button.grid(row=3, column=0, padx=10, sticky="WE")

    def convert(self):
        """Call the appropriate conversion function based off radio button values"""
        # English to morse code:
        if self.language.get() == 1:
            self.get_morse()
        elif self.language.get() == 2:
            self.get_english()

    def get_morse(self):
        """Convert an English message to morse code"""
        # String to hold morse code message
        morse_code = ""

        # Get the input text and standardize it to lower case
        text = self.input_text.get("1.0", END)
        text = text.lower()

        # Remove any letters of symbols not in our dict keys
        for letter in text:
            if letter not in self.english_to_morse.keys():
                text = text.replace(letter, '')

        # Break up into individual words based on space " " and put into a list
        word_list = text.split(" ")

        # Turn each individual word in word_list into a list of letters
        for word in word_list:
            letters = list(word)
            # For each letter, get the morse code representation and append it to the string morse_code
            for letter in letters:
                morse_char = self.english_to_morse[letter]
                morse_code += morse_char
                # Seperate individual letters with a space
                morse_code += " "
            # Seperate individual words with a |
            morse_code += "|"

        self.output_text.insert("1.0", morse_code)

    def get_english(self):
        """Convert a morse code message to english"""
        # String to hold English message
        english = ""

        # Get the input text
        text = self.input_text.get("1.0", END)

        # Remove any letters or symbols not in our dict keys
        for letter in text:
            if letter not in self.morse_to_english.keys():
                text = text.replace(letter, '')

        # Break up each word based on | and put into a list
        word_list = text.split("|")

        # Turn each word into a list of letters
        for word in word_list:
            letters = word.split(" ")
            # For each letter, get the English representation and add it to the string English
            for letter in letters:
                english_char = self.self.output_text[letter]
                english += english_char
            # seperate individual words with a space
            english += " "

        self.output_text.insert("1.0", english)

    def clear(self):
        """Clear both text fields"""
        self.input_text.delete("1.0", END)
        self.output_text.delete("1.0", END)

    def play(self):
        """Play tones for corresponding dots and dashes"""
        # Determine where the morse code is
        if self.language.get() == 1:
            text = self.output_text.get("1.0", END)
        elif self.language.get() == 2:
            text = self.input_text.get("1.0", END)

        # Play the tones (., -, " " , |)
        for value in text:
            if value == ".":
                PlaySound('dot.mp3', SND_FILENAME)
                self.after(100)
            elif value == "-":
                PlaySound('dash.mp3', SND_FILENAME)
                self.after(200)
            elif value == " ":
                self.after(300)
            elif value == "|":
                self.after(700)

    def show_guide(self):
        """Show a morse code guide in a second window"""
        # Image 'morse' needs to be a global variable to put on our window
        # Window 'guide' needs to be global to close in another function.

        # Create second window relative to the root window
        self.guide = tk.Toplevel()
        self.guide.title("Morse Guide")
        self.guide.iconbitmap(absolute_base + '/morse.ico')
        self.guide.geometry('350x350+' + str(self.winfo_x()+500) +
                            "+" + str(self.winfo_y()))
        self.guide.config(bg=self.root_color)

        # Create the image, label, and pack
        self.morse = ImageTk.PhotoImage(
            Image.open(absolute_base+'/morse_chart.jpg')
        )
        label = tk.Label(self.guide, image=self.morse, bg=self.frame_color)
        label.pack(padx=10, pady=10, ipadx=5, ipady=5)

        # Create a close button
        close_button = tk.Button(
            self.guide, text="Close", font=self.button_font,
            bg=self.button_color, command=self.hide_guide)
        close_button.pack(padx=10, ipadx=50)

        # Disabel the guide button
        self.guide_button.config(state=DISABLED)

    def hide_guide(self):
        """Hide the guide"""
        self.guide_button.config(state=NORMAL)
        self.guide.destroy()


if __name__ == "__main__":
    app = Example()
    app.mainloop()
