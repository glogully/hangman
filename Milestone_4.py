import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]  
        self.num_letters = len(set(self.word.lower())) 
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        processed_guess = guess.lower()
        
        if processed_guess in self.list_of_guesses:
            print(f"You already tried {guess}.")
            return False

        self.list_of_guesses.append(processed_guess)

        if processed_guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            new_letter_guessed = False
            for idx, letter in enumerate(self.word):
                if letter.lower() == processed_guess:
                    if self.word_guessed[idx] == '_':
                        new_letter_guessed = True
                    self.word_guessed[idx] = letter  
            if new_letter_guessed:
                self.num_letters -= 1  
            return True
        else:
            self.num_lives -= 1  
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} {'lives' if self.num_lives > 1 else 'life'} left.")
            return False
    
    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            print(' '.join(self.word_guessed))  
            guess = input("Please enter a single letter: ")

            if len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
                print(f"You have {self.num_lives} {'lives' if self.num_lives > 1 else 'life'} left.")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break


def main():
    word_list = ["Pineapple", "Pear", "Mango", "Banana", "Orange"]
    print("Word List:", word_list)
    play_game(word_list)


if __name__ == "__main__":
    main()