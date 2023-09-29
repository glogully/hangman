import random

# Create a list containing the names of your 5 favorite fruits and assign this list to a variable.
word_list = ["Pineapple", "Pear", "Mango", "Banana", "Orange"]

# Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Use the random.choice method to get a random word from word_list.
word = random.choice(word_list)

# Commenting out the debug print statement
# print("Secret Word: ", word)

def check_guess(guess, word):
    # Convert the guess into lower case.
    guess = guess.lower()
    # Check whether the guessed letter is in the secret word.
    if guess in word.lower():
        # If the guess is in the word, congratulate the user.
        print(f"Good guess! {guess} is in the word.")
    else:
        # If the guess is not in the word, inform the user.
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        # Ask the user to guess a letter and assign input to a variable called guess.
        guess = input("Please enter a single letter: ")
        
        # Check that the guess is a single alphabetical character.
        if len(guess) == 1 and guess.isalpha():
            # Call the check_guess function to check if the guess is in the word.
            check_guess(guess, word)
        # Break out of the loop. Remove this if you want the user to keep guessing until they decide to quit.
            break
        else:
            # If the guess does not pass the initial checks, inform the user to enter a single alphabetical character.
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to start the game.
ask_for_input(word)
