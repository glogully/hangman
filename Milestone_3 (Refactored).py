import random

def check_guess(guess, word):
    """Check if the guessed letter is in the word."""
    processed_guess = guess.lower()  
    processed_word = word.lower()  

    if processed_guess in processed_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input(word):
    """Keep asking the user for input until a valid single alphabetical character is entered."""
    while True:
        guess = input("Please enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, word)
            break  
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def main():
    """Main function to run the game."""
    word_list = ["Pineapple", "Pear", "Mango", "Banana", "Orange"]
    print("Word List:", word_list)

    word = random.choice(word_list)
    ask_for_input(word)


if __name__ == "__main__":
    main()