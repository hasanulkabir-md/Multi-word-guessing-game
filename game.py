import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
WORDS = [
    "python", "java", "swift", "kotlin", "javascript",
    "ruby", "scala", "typescript", "haskell", "clojure",
    "elixir", "golang", "rust", "erlang", "perl"
]

class WordGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Word Guessing Game")
        self.geometry("800x800")
        self.resizable(False, False)

        # Dictionary to store game state
        self.game_state = {
            'word_to_guess': "",
            'guessed_letters': set(),
            'incorrect_guesses': 0,
            'rounds_played': 0,
            'correct_rounds': 0,
            'game_result': None,
        }

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Frame to display the current word
        self.word_frame = tk.Frame(self)
        self.word_frame.pack(pady=20)

        # Frame to display guessed letters
        self.letters_frame = tk.Frame(self)
        self.letters_frame.pack(pady=20)

        # Frame for the keyboard buttons
        self.keyboard_frame = tk.Frame(self)
        self.keyboard_frame.pack(pady=20)
        
        # Create the keyboard buttons
        self.create_keyboard()

        # Label to display game result
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

        # Button to play again
        self.play_again_button = tk.Button(self, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

        # Load the first word to guess
        self.load_word_to_guess()

    def create_keyboard(self):
        # Define keyboard buttons
        buttons = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M'
        ]
        
        # Create and pack the keyboard buttons
        for button in buttons:
            btn = tk.Button(self.keyboard_frame, text=button, command=lambda b=button: self.guess(b))
            btn.pack(side=tk.LEFT)

    def guess(self, letter):
        # Check for valid input (single letter)
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        # Handle a guessed letter
        self.game_state['guessed_letters'].add(letter.lower())

        # Check if the guessed letter is in the word
        if letter.lower() in self.game_state['word_to_guess']:
            self.handle_correct_guess()
        else:
            self.handle_incorrect_guess()

    def handle_correct_guess(self):
        # Update display and check if all letters are guessed
        self.update_display()

        if all(letter in self.game_state['guessed_letters'] for letter in self.game_state['word_to_guess']):
            # Player has guessed the word correctly
            self.game_state['game_result'] = "Congratulations! You have won!"
            self.game_state['rounds_played'] += 1
            self.game_state['correct_rounds'] += 1
            self.play_again_button.config(state=tk.NORMAL)
            # Show a message box with the game result
            messagebox.showinfo("Game Over", "Congratulations! You have won!")
        else:
            self.game_state['game_result'] = "Good guess!"

        self.update_result_label()

    def handle_incorrect_guess(self):
        # Handle an incorrect guess
        self.game_state['incorrect_guesses'] += 1

        if self.game_state['incorrect_guesses'] >= 8:
            # Player has reached the maximum incorrect guesses
            self.game_state['game_result'] = f"Sorry, you've reached the maximum incorrect guesses. The correct word was: {self.game_state['word_to_guess']}"
            self.game_state['rounds_played'] += 1
            self.play_again_button.config(state=tk.NORMAL)
            # Show a message box with the game result
            messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum incorrect guesses. The correct word was: {self.game_state['word_to_guess']}")
        else:
            self.game_state['game_result'] = f"Incorrect guess! Attempts left: {8 - self.game_state['incorrect_guesses']}"

        self.update_result_label()
        self.update_display()

    def load_word_to_guess(self):
        # Load a new word to guess
        self.game_state['guessed_letters'] = set()
        self.game_state['incorrect_guesses'] = 0
        self.game_state['word_to_guess'] = random.choice(WORDS)
        self.game_state['game_result'] = None

        self.update_result_label()
        self.update_display()

    def update_display(self):
        # Update the displayed word and guessed letters
        for widget in self.word_frame.winfo_children():
            widget.destroy()

        for letter in self.game_state['word_to_guess']:
            letter_label = tk.Label(self.word_frame, text=" ".join(
                letter.upper() if letter in self.game_state['guessed_letters'] else '_'))
            letter_label.pack(side=tk.LEFT)

        for widget in self.letters_frame.winfo_children():
            widget.destroy()

        letters_label = tk.Label(self.letters_frame, text=" ".join(sorted(self.game_state['guessed_letters'])))
        letters_label.pack()

    def update_result_label(self):
        # Update the label displaying the game result
        self.result_label.config(text=self.game_state['game_result'] or "")

    def play_again(self):
        # Reset the game to play again
        self.play_again_button.config(state=tk.DISABLED)
        self.load_word_to_guess()

# Run the game
if __name__ == "__main__":
    app = WordGuessingGame()
    app.mainloop()
