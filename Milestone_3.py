while True:
    #Ask the user to guess a letter
    guess = input("Please enter a single letter: ")
    
    #Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        #If the guess passes the checks, break out of the loop
        print("Good guess!")
        break
    else:
        # If the guess does not pass the checks
        print("Invalid letter. Please, enter a single alphabetical character.")