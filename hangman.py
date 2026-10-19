
import random

WORDS = [
    "PYTHON",
    "COMPUTER",
    "PROGRAMMING",
    "DEVELOPER",
    "SCIENCE",
    "KEYBOARD",
    "INTERNET",
    "SOFTWARE"
]

HANGMAN = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n=== HANGMAN GAME ===")
    print("Guess the hidden word one letter at a time!")

    while wrong_guesses < max_attempts:
        print(HANGMAN[wrong_guesses])

        display_word = [
            letter if letter in guessed_letters else "_"
            for letter in word
        ]

        print("Word:", " ".join(display_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Incorrect guesses:", wrong_guesses, "/", max_attempts)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter one letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    print(HANGMAN[wrong_guesses])
    print("You lost! The word was:", word)


def main():
    while True:
        play_hangman()

        again = input("Play again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
