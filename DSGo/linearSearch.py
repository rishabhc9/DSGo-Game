

import tkinter as tk
from tkinter import messagebox
from random import sample
from typing import Optional


class Game:
    def __init__(self: object):
        # Setting default values and creating the 5 coloured buttons at the bottom of the Frame
        self.canvas = tk.Canvas(win, bg='grey', width=310, height=500)
        self.canvas.grid(rowspan=8, columnspan=5)
        self.row = 10
        self.column = 1
        self.colours = ['red', 'orange', 'yellow', 'green', 'blue']
        self.pattern = sample(self.colours, len(self.colours))
        self.guessCoordinates = [10, 440, 60, 490]
        self.incorrectCoordinates = [10, 440, 60, 490]
        self.check = -1
        self.guess = []
        self.guesses = []
        self.choice = None
        for i in range(len(self.colours)):
            self.button = tk.Button(frame, bg=self.colours[i], width=6, height=3, bd=4,
                                    command=lambda colour=self.colours[i]: self.AddGuess(colour, self.guessCoordinates))
            self.button.grid(row=1, column=i, padx=(0, 4), pady=(0, 4))
        return

    def AddGuess(self: object, colour: str, coordinates: list):
        # Adds the correct coloured guess to the canvas
        # Adds the guess to a list of guessed colours
        # Updates the coordinates for the next guess
        if coordinates[1] + 60 and coordinates[3] == 70:
            return
        self.choice = self.canvas.create_oval(coordinates, outline='black', fill=colour, tags=colour)
        self.guesses.append(self.canvas.gettags(self.choice)[0])
        self.UpdateCoordinates(coordinates)

    def UpdateCoordinates(self: object, Coordinates: list) -> Optional[list]:
        # Moves the coordinates over by 50 so the guess don't overlap
        # Moves the guesses up to the next row if the are 5 of them
        if Coordinates[0] + 60 and Coordinates[2] == 300:
            Coordinates[0] = 10
            Coordinates[2] = 60
            Coordinates[1] -= 60
            Coordinates[3] -= 60
            self.CheckGuess()
            return None
        else:
            Coordinates[0] = Coordinates[0] + 60
            Coordinates[2] = Coordinates[2] + 60
        return Coordinates

    def CheckGuess(self: object):
        self.check += 1
        # Goes through the row to find out if any guess are right
        # If they are a WIN window pops up and the current game ends
        if self.guesses == self.pattern:
            tk.messagebox._show('WIN', 'You found the correct order. Congratulations! You have learned the concept of Linear Search.')
            self.guess = []
            return
        else:
            for i in range(len(self.guesses)):
                if self.guesses[i] != self.pattern[i]:
                    self.ShowCorrectGuesses(i, self.check)
            self.guesses = []

    def ShowCorrectGuesses(self: object, position: int, row: int):
        # Displays a black circle over the incorrectly guessed colours
        coordinates = [10, 440, 60, 490]
        Position = position * 60
        Row = row * 60
        coordinates[0] = coordinates[0] + Position
        coordinates[1] = coordinates[1] - Row
        coordinates[2] = coordinates[2] + Position
        coordinates[3] = coordinates[3] - Row
        self.choice = self.canvas.create_oval(coordinates, outline='black', fill='black')


# Main program
if __name__ == '__main__':
    # Window Widgets
    win = tk.Tk()
    win.title('Mastermind Game')
    label = tk.Label(text='Mastermind Game', font=("Helvetica", 18))
    frame = tk.Frame(win)
    # Game Object
    mastermind = Game()
    # Displaying the Widgets
    label.grid(row=1, columnspan=5)
    frame.grid(row=10, columnspan=5)
    # Run the code infinitely
    win.mainloop()
