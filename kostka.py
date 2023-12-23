import tkinter as tk
from tkinter import Label, Button
import random


class Dice:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Simulator")

        self.label = Label(self.master, text="Roll the dice", font=("Helvetica", 24), bg="#6D9DC5", fg="#B0E298")
        self.label.grid(row=0, column=0)

        self.rollButton = Button(self.master, text="Roll the dice", command=self.Roll)
        self.rollButton.grid(row=1, column=0)

    def Roll(self):
        result = random.randint(1, 6)
        self.label.config(text=str(result))


if __name__ == "__main__":
    root = tk.Tk()
    dice = Dice(root)
    root.mainloop()
