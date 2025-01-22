import tkinter as tk
import random

class GuessTheNumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        
        # counts for player guesses
        self.guess_count = 0
        self.guesses_left = 5

        # Number for player to Guess
        self.min_number = 1
        self.max_number = 100
        self.target_number = random.randint(self.min_number, self.max_number)

        # Labels and input for the player to interact with the game
        self.label_description = tk.Label(root, text=f"Guess a number between {self.min_number} and {self.max_number}")
        self.label_description.pack()

        self.label_counter = tk.Label(root, text=f"Number of Guesses Left: {self.guesses_left}")
        self.label_counter.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command = self.checkGuess)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.reset_button = tk.Button(root, text = "Reset", command=self.resetGame)
        self.reset_button.pack()

    # check the guess of the player and decrement the number of guesses the player has. 
    def checkGuess(self):
        # catch an exception if the player inputs something that is not a Valid number
        try:
            guess = int(self.entry.get())
            self.guess_count += 1
            self.guesses_left -= 1

            # set the win lose and try again rules here
            if guess < self.target_number:
                self.result_label.config(text = f"{guess} is Too Low! Try again.")
                self.entry.delete(0, tk.END)
            elif guess > self.target_number:
                self.result_label.config(text = f"{guess} is Too High, Try again.")
                self.entry.delete(0, tk.END)            
            else:
                self.result_label.config(text = "Congrats you guessed the number!")

            # set the lose rules for taking to many turns
            if self.guess_count > 4:
                self.result_label.config(text = "Game Over. You guessed to many times please play again.")
            self.label_counter.config(text = f"Number of Guesses Left: {self.guesses_left}")

        except ValueError:
            self.result_label.config(text = "You did not enter a Valid Number.")
    
    # reset the game to play multiple times whether we win or lose
    def resetGame(self):
        self.target_number = random.randint(self.min_number, self.max_number)
        self.guess_count = 0
        self.guesses_left = 5
        self.label_counter.config(text = f"Number of Guesses Left: {self.guesses_left}")
        self.result_label.config(text = "")
        self.entry.delete(0, tk.END) 

# allow us to play the game
if __name__ == '__main__':
    root = tk.Tk()
    game = GuessTheNumber(root)
    root.mainloop()


