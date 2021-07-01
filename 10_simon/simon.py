import tkinter as tk
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random
from os import path

absolute_base = path.dirname(path.realpath(__file__))


class Example(tk.Tk):
    game_font1 = ('Arial', 12)
    game_font2 = ('Arial', 8)
    white = "#c6cbcd"
    white_light = "#fbfcfc"
    magenta = "#90189e"
    magenta_light = "#f802f9"
    cyan = "#078384"
    cyan_light = "#00fafa"
    yellow = "#9ba00f"
    yellow_light = "#f7f801"
    root_color = "#2eb4c6"
    game_color = "#f6f7f8"

    def __init__(self):
        super().__init__()
        self.title('Simon Memory Game')
        self.iconbitmap(absolute_base + '\simon.ico')
        self.geometry('400x400')
        self.resizable(0, 0)

        # sett global variables for the game
        self.time = 500
        self.score = 0
        self.game_sequence = []
        self.player_sequence = []

        self.setup_ui()

    def setup_ui(self):
        # Define Layout
        # Create frames
        info_frame = tk.Frame(self, bg=self.root_color)
        game_frame = tk.LabelFrame(self, bg=self.game_color)
        info_frame.pack(pady=(10, 20))
        game_frame.pack()

        # Layout for the info frame
        self.start_button = tk.Button(
            info_frame, text="New Game", font=self.game_font1,
            bg=self.game_color, command=self.enable)
        self.score_label = tk.Label(
            info_frame, text="Score: " + str(self.score),
            font=self.game_font1, bg=self.root_color)
        self.start_button.grid(row=0, column=0, padx=20, ipadx=30)
        self.score_label.grid(row=0, column=1)

        # Layout for the game frame
        # Make the game buttons
        self.white_button = tk.Button(game_frame, bg=self.white,
                                      activebackground=self.white_light,
                                      borderwidth=3, state=DISABLED,
                                      command=lambda: self.press(1))
        self.magenta_button = tk.Button(game_frame, bg=self.magenta,
                                        activebackground=self.magenta_light,
                                        borderwidth=3, state=DISABLED,
                                        command=lambda: self.press(2))
        self.cyan_button = tk.Button(game_frame, bg=self.cyan,
                                     activebackground=self.cyan_light,
                                     borderwidth=3, state=DISABLED,
                                     command=lambda: self.press(3))
        self.yellow_button = tk.Button(game_frame, bg=self.yellow,
                                       activebackground=self.yellow_light,
                                       borderwidth=3, state=DISABLED,
                                       command=lambda: self.press(4))

        self.white_button.grid(row=0, column=0, columnspan=2,
                               padx=10, pady=10, ipadx=60, ipady=50)
        self.magenta_button.grid(row=0, column=2, columnspan=2,
                                 padx=10, pady=10, ipadx=60, ipady=50)
        self.cyan_button.grid(row=1, column=0, columnspan=2,
                              padx=10, pady=10, ipadx=60, ipady=50)
        self.yellow_button.grid(row=1, column=2, columnspan=2,
                                padx=10, pady=10, ipadx=60, ipady=50)

        # Make radio buttons for difficulty
        self.difficulty = StringVar()
        self.difficulty.set('Medium')
        tk.Label(game_frame, text='Difficulty:', font=self.game_font2,
                 bg=self.game_color).grid(row=2, column=0)
        tk.Radiobutton(game_frame, text="Easy", variable=self.difficulty,
                       value="Easy",
                       font=self.game_font2, bg=self.game_color,
                       command=self.set_difficulty).grid(row=2, column=1)
        tk.Radiobutton(game_frame, text="Medium",
                       variable=self.difficulty, value="Medium",
                       font=self.game_font2, bg=self.game_color,
                       command=self.set_difficulty).grid(row=2, column=2)
        tk.Radiobutton(game_frame, text="Hard",
                       variable=self.difficulty, value="Hard",
                       font=self.game_font2, bg=self.game_color,
                       command=self.set_difficulty).grid(row=2, column=3)

    def pick_sequence(self):
        """
        Pick the next value in the sequence.  Do not allow for repeated values.
        """
        while True:
            value = random.randint(1, 4)
            # Sequence is size 0, so take the value regardless
            if len(self.game_sequence) == 0:
                self.game_sequence.append(value)
                break
            # make sure the current value is not the same as the last value
            # in the sequence
            elif value != self.game_sequence[-1]:
                self.game_sequence.append(value)
                break

        # Now that the value is added to the sequence, play the sequence
        self.play_sequence()

    def play_sequence(self):
        """
        Play the entire sequence for a given round by animating the buttons
        """
        # Change button label
        self.change_label("Playing!")

        # Without delay, all buttons will animate at the same time.  The delay
        # adds the 'time' variable to each .after()
        delay = 0
        for value in self.game_sequence:
            if value == 1:
                self.after(delay, lambda: self.animate(self.white_button))
            elif value == 2:
                self.after(delay, lambda: self.animate(self.magenta_button))
            elif value == 3:
                self.after(delay, lambda: self.animate(self.cyan_button))
            elif value == 4:
                self.after(delay, lambda: self.animate(self.yellow_button))

            # Increment delay for next iteration of loop
            delay += self.time

    def animate(self, button):
        """Animate a given button by chaning its color"""
        button.config(state=ACTIVE)
        self.after(self.time, lambda: button.config(state=NORMAL))

    def change_label(self, message):
        """
        Update the start button text and color to let the player know 
        their status.
        """
        self.start_button.config(text=message)

        if message == "Wrong!":
            self.start_button.config(bg='red')
        else:
            self.start_button.config(bg=self.game_color)

    def set_difficulty(self):
        """
        Use radio buttons to set difficulty.  Difficulty affects time between 
        button 'flashes
        '"""

        # Change the time (difficulty) based off the value of the radio buttons
        if self.difficulty.get() == 'Easy':
            self.time = 1000
        elif self.difficulty.get() == 'Medium':
            self.time = 500
        else:
            self.time = 200

    def press(self, value):
        """Simulate pressing a button for player."""
        # Add the players press to players sequence
        self.player_sequence.append(value)

        # If the current 'round' is over, check to see if the player enter
        # the correct sequence of button presses
        if len(self.player_sequence) == len(self.game_sequence):
            self.check_round()

    def check_round(self):
        """
        Determine if the player entered the correct sequence of button 
        presses for a round.
        """

        # The player is correct, so change the label, update score,
        # wait, then start the next round.
        if self.player_sequence == self.game_sequence:
            self.change_label("Correct!")
            self.score += len(self.player_sequence) + int(1000/self.time)
            self.after(500, self.pick_sequence)
        # The player is incorrect so change label, update score, disable
        # buttons, and reset for new game.
        else:
            self.change_label('Wrong!')
            self.score = 0
            self.disable()
            # The game is over, so wipe the game sequence
            self.game_sequence = []
            # Wait 2 seconds then change the message
            self.after(2000, lambda: self.change_label("New Game"))

        # Regardless of win or lose for a round, wipe the players sequence
        self.player_sequence = []

        # Update score label
        self.score_label.config(text="Score: " + str(self.score))

    def disable(self):
        """Dislabe all buttons so they can't accidentally be pressed."""
        self.white_button.config(state=DISABLED)
        self.magenta_button.config(state=DISABLED)
        self.cyan_button.config(state=DISABLED)
        self.yellow_button.config(state=DISABLED)

    def enable(self):
        """Enable all buttons to start the game and pick the first value in the sequence."""
        self.white_button.config(state=NORMAL)
        self.magenta_button.config(state=NORMAL)
        self.cyan_button.config(state=NORMAL)
        self.yellow_button.config(state=NORMAL)

        # Pick a value!
        self.pick_sequence()


if __name__ == "__main__":
    app = Example()
    app.mainloop()
