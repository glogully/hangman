import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.num_letters = len(set(self.word.lower()))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        processed_guess = guess.lower()

        if processed_guess in self.list_of_guesses:
            print(f"You already tried {guess}.")
            return

        self.list_of_guesses.append(processed_guess)

        if processed_guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            self.word_guessed = [letter if letter.lower() == processed_guess else curr for letter, curr in zip(self.word, self.word_guessed)]
            self.num_letters = sum(1 for char in self.word_guessed if char == '_')

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} {'lives' if self.num_lives > 1 else 'life'} left.")

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            print(' '.join(self.word_guessed))
            guess = input("Please enter a single letter: ")

            if len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        self.end_game_message()

    def end_game_message(self):
        if self.num_letters == 0:
            print("Congratulations. You won the game!")
        else:
            print("You lost! The word was:", self.word)


def play_game(word_list):
    game = Hangman(word_list)
    game.ask_for_input()


def main():
    word_list = ["Pineapple", "Pear", "Mango", "Banana", "Orange"]
    print("Word List:", word_list)
    play_game(word_list)


if __name__ == "__main__":
    main()