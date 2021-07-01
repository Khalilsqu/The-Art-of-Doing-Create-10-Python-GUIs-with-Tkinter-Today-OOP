import tkinter as tk
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):
    my_font = ('Times New Roman', 12)
    self_color = '#6c1cbc'
    button_color = '#e2cff4'

    def __init__(self):
        super().__init__()
        self.title('Simple Checklist')
        self.iconbitmap(absolute_base + '/check.ico')
        self.geometry('400x400')
        self.resizable(0, 0)
        self.config(bg=self.self_color)

        self.setup_ui()

    def setup_ui(self):
        # Define layout
        # Create frames
        input_frame = tk.Frame(self, bg=self.self_color)
        output_frame = tk.Frame(self, bg=self.self_color)
        button_frame = tk.Frame(self, bg=self.self_color)
        input_frame.pack()
        output_frame.pack()
        button_frame.pack()

        # Input frame layout
        self.list_entry = tk.Entry(
            input_frame, width=35, borderwidth=3, font=self.my_font)
        self.list_entry.focus_set()
        list_add_button = tk.Button(
            input_frame, text="Add Item", borderwidth=2, font=self.my_font,
            bg=self.button_color, command=self.add_item)
        self.list_entry.grid(row=0, column=0, padx=5, pady=5)
        list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

        # Output frame layout
        my_scrollbar = tk.Scrollbar(output_frame)
        self.my_listbox = tk.Listbox(output_frame, height=15, width=45,
                                     borderwidth=3, font=self.my_font,
                                     yscrollcommand=my_scrollbar.set)
        # Link scrollbar to listbox
        my_scrollbar.config(command=self.my_listbox.yview)
        self.my_listbox.grid(row=0, column=0)
        my_scrollbar.grid(row=0, column=1, sticky="NS")

        # Button Frame layout
        list_remove_button = tk.Button(button_frame, text="Remove Item", borderwidth=2,
                                       font=self.my_font, bg=self.button_color,
                                       command=self.remove_item)
        list_clear_button = tk.Button(button_frame, text='Clear List',
                                      borderwidth=2, font=self.my_font,
                                      bg=self.button_color, command=self.clear_list)
        save_button = tk.Button(button_frame, text='Save List', borderwidth=2,
                                font=self.my_font, bg=self.button_color,
                                command=self.save_list)
        quit_button = tk.Button(button_frame, text='Quit', borderwidth=2,
                                font=self.my_font, bg=self.button_color,
                                command=self.destroy)
        list_remove_button.grid(row=0, column=0, padx=2, pady=10)
        list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
        save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
        quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

        self.open_list()
        self.bind("<Return>", self.add_item)

    def add_item(self, event=None):
        """Add an individual item to the listbox"""
        text = self.list_entry.get()
        if text:
            self.my_listbox.insert(tk.END, text)
            self.list_entry.delete(0, tk.END)

    def remove_item(self):
        """Remove the selected (ANCHOR) item from the listbox"""
        self.my_listbox.delete(tk.ANCHOR)

    def clear_list(self):
        """Delete all items from the listbox"""
        self.my_listbox.delete(0, tk.END)

    def save_list(self):
        """Save the list to a simple txt file"""
        with open('checklist.txt', 'w') as f:
            # listbox.get() returns a tuple....
            list_tuple = self.my_listbox.get(0, tk.END)
            for item in list_tuple:
                # Take proper precautions to include only one \n
                # for formatting purposes
                if item.endswith('\n'):
                    f.write(item)
                else:
                    f.write(item + "\n")

    def open_list(self):
        """Open the list upon starting the program if there is one"""
        try:
            with open('checklist.txt', 'r') as f:
                for line in f:
                    self.my_listbox.insert(tk.END, line)
        except:
            return


if __name__ == "__main__":
    app = Example()
    app.mainloop()
