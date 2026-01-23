import random

# List of words with hints (dictionary = word : hint)
words_with_hints = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "keyboard": "Used to type",
    "internet": "Connects the world",
    "hangman": "This game itself"
}

# Randomly choose a word
word = random.choice(list(words_with_hints.keys()))
hint = words_with_hints[word]

# Game variables
guessed_letters = []
wrong_guesses = []
attempts = 6

print(" WELCOME TO HANGMAN GAME")
print("Hint:", hint)

# Function to display current word progress
def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Game loop
while attempts > 0:
    print("\nWord:", display_word())
    print("Wrong guesses:", wrong_guesses)
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter.")
        continue

    # Correct guess
    if guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")

        # Check if user won
        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break

    # Wrong guess
    else:
        wrong_guesses.append(guess)
        attempts -= 1
        print("Wrong guess!")

# If attempts are over
if attempts == 0:
    print("\n Game Over!")
    print("The word was:", word)