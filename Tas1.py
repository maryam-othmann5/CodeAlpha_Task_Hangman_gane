# task 1 : Hangman Game
import random

def choose_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts_left = 6  # Set a limit of 6 incorrect guesses

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts_left -= 1

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

        if attempts_left == 0:
            print("\nSorry, you ran out of attempts. The word was:", word)
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

# Start the game
hangman()