# Multi-Word Guessing Game

## Overview

The **Multi-Word Guessing Game** is a fun, interactive game similar to the classic **Hangman**. In this game, players are tasked with guessing a series of words, one letter at a time. With each incorrect guess, a new word is added to the list. The objective is to guess the letters of the words correctly with the fewest number of incorrect guesses.

To win, players must guess all the letters in the displayed words before reaching 8 incorrect guesses. The fewer words shown and the fewer incorrect guesses made, the higher the score.

## Features

* **Guessing Mechanism**: The player guesses one letter at a time, and the game displays the guessed letter in the correct place if it’s part of the word.
* **Multiple Words**: When the player guesses a letter incorrectly, a new word is added to the game, increasing the challenge.
* **Score Tracking**: The player’s score is determined by how many words are shown, with a lower score being better.
* **Game Over**: The game ends when the player reaches 8 incorrect guesses. The correct words will then be displayed.

## Requirements

* Python 3.x
* tkinter library (usually comes pre-installed with Python)

## Installation

1. Clone or download the project repository.
2. Make sure you have Python 3.x installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
3. Ensure that `tkinter` is available on your system. If you're using Python 3.x, it should be installed by default.

## Running the Game

1. Download or clone the repository.
2. Navigate to the folder containing the project files.
3. Run the game using the following command:

```bash
python game.py
```

The game window will appear, and you can begin playing!

## How to Play

* **Guessing**: The game will display underscores (`_`) representing the letters in each word. You will be prompted to guess one letter at a time.
* **Correct Guess**: If your guessed letter is correct, it will be displayed in the corresponding positions of the word.
* **Incorrect Guess**: If your guessed letter is incorrect, a new word will be added to the game. You have a maximum of 8 incorrect guesses before the game ends.
* **Winning**: To win, you need to guess all the letters in all the words without exceeding the 8 incorrect guesses.
* **Play Again**: After the game ends, you can click the "Play Again" button to restart with a new set of words.

## Scoring

* Your score is the number of words displayed during the game.
* Fewer incorrect guesses and fewer words shown lead to a better score.

## Example Gameplay

1. The game starts with one word and a series of underscores representing the word.
2. You guess a letter, for example, `E`.

   * If `E` is in the word, it will be displayed in the correct positions.
   * If `E` is not in the word, a new word is added to the game.
3. The game continues with the player guessing letters until they either win by guessing all letters or lose by reaching 8 incorrect guesses.

## Sample Screenshot

![Game Screenshot](link_to_screenshot.jpg)

## Game Over

The game ends when:

* The player guesses all the letters in all the words correctly.
* The player reaches 8 incorrect guesses.

### Example Message After Losing:

```
Sorry, you've reached the maximum incorrect guesses. The correct words were: python, java, kotlin
```

### Example Message After Winning:

```
Congratulations! You have won! You guessed all the letters in the words correctly.
```

## Contributing

Feel free to fork this project, submit issues, and send pull requests! Contributions are welcome.

## License

This project is open-source and available under the MIT License.

---
