import random

def choose_word():
    words = ["python", "java", "programmer", "computer_List", "keyboard", "developer", "Tester", "alphabet", "vaiable", "software","Manoj","swapnodaya"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")

    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 3

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Current word: {current_display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}")

        if "_" not in current_display:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
            else:
                print("Incorrect guess.")
                attempts_left -= 1

            guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        if attempts_left == 0:
            print(f"Sorry, you ran out of attempts. The word was '{secret_word}'.")
            break

if __name__ == "__main__":
    hangman()
