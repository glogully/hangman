# Create a list containing the names of your 5 favorite fruits.
fruits = ["Pineapple", "Pear", "Mango", "Banana", "Orange"]


#Assign this list to a variable called word_list.
word_list = fruits


#Print out the newly created list to the standard output (screen).
print(word_list)


#Use Random import
import random


# Use the random.choice method to get a random word from word_list and assign it to the variable word
word = random.choice(word_list)


# Print out the randomly chosen word to the standard output (screen).
print(word)
#Use input function to ask user to enter a single letter and assign input to a variable called guess.
guess = input("Please enter a single letter: ")



#Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    #Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")
