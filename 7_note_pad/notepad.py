import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext, font
from PIL import ImageTk, Image
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):
    # Define fonts and colors
    text_color = "#fffacd"
    menu_color = "#dbd9db"
    root_color = "#6c809a"

    def __init__(self):
        super().__init__()
        self.title('Notepad')
        self.iconbitmap(absolute_base + '/pad.ico')
        self.geometry('600x600')
        self.resizable(0, 0)
        self.config(bg=self.root_color)

        self.setup_ui()

    def setup_ui(self):
        # Define Layout
        # Define frames
        menu_frame = tk.Frame(self, bg=self.menu_color)
        text_frame = tk.Frame(self, bg=self.text_color)
        menu_frame.pack(padx=5, pady=5)
        text_frame.pack(padx=5, pady=5)

        # Layout for menu frame
        # Create the menu:  new, open, save, close, font family, font size,
        # font option
        self.new_image = ImageTk.PhotoImage(
            Image.open(absolute_base + '/new.png'))
        new_button = tk.Button(
            menu_frame, image=self.new_image, command=self.new_note)
        CreateToolTip(new_button, "Create New Notepad")
        new_button.grid(row=0, column=0, padx=5, pady=5)

        self.open_image = ImageTk.PhotoImage(
            Image.open(absolute_base + '/open.png'))
        open_button = tk.Button(
            menu_frame, image=self.open_image, command=self.open_note)
        CreateToolTip(open_button, "Open Existing Notepad")
        open_button.grid(row=0, column=1, padx=5, pady=5)

        self.save_image = ImageTk.PhotoImage(
            Image.open(absolute_base + '/save.png'))
        save_button = tk.Button(
            menu_frame, image=self.save_image, command=self.save_note)
        CreateToolTip(save_button, "Save Notepad")
        save_button.grid(row=0, column=2, padx=5, pady=5)

        self.close_image = ImageTk.PhotoImage(
            Image.open(absolute_base + '/close.png'))
        close_button = tk.Button(
            menu_frame, image=self.close_image, command=self.close_note)
        CreateToolTip(close_button, "Close Notepad")
        close_button.grid(row=0, column=3, padx=5, pady=5)

        # Create a list of fonts to use
        families = font.families()

        self.font_family = tk.StringVar()
        self.font_family_drop = tk.OptionMenu(
            menu_frame, self.font_family, *families, command=self.change_font)
        CreateToolTip(self.font_family_drop, "Change font family")
        self.font_family.set('Terminal')
        # Set the width so it will fit "times new roman" and remain constant
        self.font_family_drop.config(width=16)
        self.font_family_drop.grid(row=0, column=4, padx=5, pady=5)

        sizes = list(range(6, 100, 4))
        self.font_size = tk.IntVar()
        self.font_size_drop = tk.OptionMenu(
            menu_frame, self.font_size, *sizes, command=self.change_font)
        self.font_size.set(12)
        # Set width to be constant even if its 8.
        self.font_size_drop.config(width=2)
        self.font_size_drop.grid(row=0, column=5, padx=5, pady=5)

        options = ['none', 'bold', 'italic']
        self.font_option = tk.StringVar()
        self.font_option_drop = tk.OptionMenu(
            menu_frame, self.font_option, *options, command=self.change_font)
        self.font_option.set('none')
        # Set the width to be constant
        self.font_option_drop.config(width=5)
        self.font_option_drop.grid(row=0, column=6, padx=5, pady=5)

        # Layout for the text frame
        my_font = (self.font_family.get(), self.font_size.get())

        # Create input_text as a scrolltext so you can scroll through the text
        # field.
        # Set default width and height to be more than the window size so that
        # on the smallest text size, the text field size is constant.
        self.input_text = scrolledtext.ScrolledText(
            text_frame, width=1000, height=100,
            bg=self.text_color, font=my_font)
        self.input_text.pack()

    def change_font(self, event):
        """Change the given font based off dropbox options."""
        if self.font_option.get() == 'none':
            my_font = (self.font_family.get(), self.font_size.get())
        else:
            my_font = (self.font_family.get(), self.font_size.get(),
                       self.font_option.get())

        # Change the font style
        self.input_text.config(font=my_font)

    def new_note(self):
        """Create a new Note which essentially clears the screen."""
        # Use a messagebox to ask for a new note
        question = messagebox.askyesno(
            "New Note", "Are you sure you want to start a new note?")
        if question == 1:
            # ScrolledText widgets starting index is 1.0 not 0.
            self.input_text.delete("1.0", tk.END)

    def close_note(self):
        """Closes the note which essentially quits the program."""
        # Use a messagebox to ask to close
        question = messagebox.askyesno(
            "Close Note", "Are you sure you want to close your note?")
        if question == 1:
            self.destroy()

    def save_note(self):
        """
        Save the given note.  First three lines are saved as font family,
        font size, and font option.
        """
        # Use filedialog to get location and name of where/what to save the
        # file as.
        save_name = filedialog.asksaveasfilename(
            initialdir="./", title="Save Note",
            filetypes=(("Text Files", "*.txt"),
                       ("All Files", "*.*")))
        with open(save_name, 'w') as f:
            # First three lines of save file are self.font_family, font_size, and
            # self.font_options.  Font_size must be a string noot int.
            f.write(self.font_family.get() + "\n")
            f.write(str(self.font_size.get()) + "\n")
            f.write(self.font_option.get() + "\n")

            # write remaining text in field to the file
            f.write(self.input_text.get("1.0", tk.END))

    def open_note(self):
        """
        Open a previously saved note.  First three lines of note are font
        family, font size, and font option.  First set the font, then load
        the text."""
        # Use filedialog to get location and directory of note file
        open_name = filedialog.askopenfilename(
            initialdir="./", title='Open Note',
            filetypes=(("Text Files", "*.txt"),
                       ("All Files", "*.*")))
        with open(open_name, 'r') as f:
            # Clear the current text
            self.input_text.delete("1.0", tk.END)

            # First three lines are font_faimly, font_size, and
            # self.font_option...You must strip the new line char at the end of
            # each line!
            self.font_family.set(f.readline().strip())
            self.font_size.set(int(f.readline().strip()))
            self.font_option.set(f.readline().strip())

            # Call the change font for these .set() and pass an arbitrary value
            self.change_font(1)

            # Read the rest of the file and insert it into the text field
            text = f.read()
            self.input_text.insert("1.0", text)


class CreateToolTip:
    '''
    create a tooltip for a given widget
    '''

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):

        x = self.widget.winfo_pointerx()
        y = self.widget.winfo_pointery()
        # x = y = 0
        # x, y, cx, cy = self.widget.bbox("insert")
        # x += self.widget.winfo_rootx() + 25
        # y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background='yellow', relief='solid', borderwidth=1,
                         font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


if __name__ == "__main__":
    app = Example()
    app.mainloop()
