import random

def choose_word():
    """
    Choose a random word from a predefined list.
    """
    words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "learning", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Display the word with blanks for unguessed letters.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    # Choose a random word
    secret_word = choose_word()

    # Initialize variables
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6  # You can customize the number of allowed incorrect attempts

    print("Welcome to Hangman!")
    
    while True:
        # Display the current state of the word
        current_display = display_word(secret_word, guessed_letters)
        print(f"\nWord: {current_display}")

        # Check if the player has guessed all letters
        if "_" not in current_display:
            print("Congratulations! You guessed the word.")
            break

        # Prompt the player to guess a letter
        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Update guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in secret_word:
            incorrect_attempts += 1
            print(f"Incorrect guess! Attempts remaining: {max_attempts - incorrect_attempts}")
            
            # Check if the player has reached the maximum allowed incorrect attempts
            if incorrect_attempts == max_attempts:
                print("Game over! You've run out of attempts.")
                print(f"The correct word was: {secret_word}")
                break

    print("Thanks for playing!")

if __name__ == "__main__":
    # Run the Hangman game
    hangman()
