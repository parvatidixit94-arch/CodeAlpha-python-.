import random

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[attempts]

words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "software"
]

word = random.choice(words)
guessed_letters = []
attempts = 6

player_name =input("enter your name:")
print("welcome", player_name )

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)

while attempts > 0:

    print(display_hangman(attempts))
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", " ".join(guessed_letters))

    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue 


    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(" Wrong Guess!")
        print("Attempts Remaining:", attempts)
    else:
        print(" Correct Guess!")

if attempts == 0:
    print(display_hangman(attempts))
    print("\n Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")