# Hangman Game

Welcome to the Hangman Game! This Python program lets you play the classic word-guessing game.

## How to Play

1. Run the script.
2. The program will choose a random word, and you need to guess the letters.
3. Enter a letter when prompted.
4. Keep guessing until you either complete the word or reach the maximum allowed incorrect attempts.

## Features

### `choose_word()` Function

- Selects a random word from a predefined list.

### `display_word(word, guessed_letters)` Function

- Displays the current state of the word with blanks for unguessed letters.

### `hangman()` Function

- Implements the main game logic.
- Initializes variables, including the secret word, guessed letters, and incorrect attempts.
- Prompts the player to guess letters until the game ends.

## Usage

```bash
python hangman.py
```

Follow the on-screen instructions to guess the word.

## Customization

- You can customize the list of words in the `choose_word` function.
- Adjust the maximum allowed incorrect attempts in the `hangman` function.

## Author

Jeel patel 
