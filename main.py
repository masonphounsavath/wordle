import random

# define the word to be guessed
word = "hello"

# convert the word to a list of characters
word_list = list(word)

# create an empty list to store the guesses
guesses = []

# define the maximum number of guesses allowed
max_guesses = 6

# loop until the word is guessed or the maximum number of guesses is reached
while len(guesses) < max_guesses:
    # ask the user for a guess
    guess = input("Guess a 5-letter word: ")

    # convert the guess to a list of characters
    guess_list = list(guess)

    # check if the guess is valid (i.e., it has the same length as the word and contains only lowercase letters)
    if len(guess_list) != len(word_list) or not all(c.islower() for c in guess_list):
        print("Invalid guess! Please enter a 5-letter word with lowercase letters.")
        continue

    # add the guess to the list of guesses
    guesses.append(guess_list)

    # check if the guess is correct
    if guess_list == word_list:
        print("Congratulations, you guessed the word!")
        break

    # generate feedback for the guess
    feedback = []
    for i in range(len(word_list)):
        if guess_list[i] == word_list[i]:
            feedback.append("O")
        elif guess_list[i] in word_list:
            feedback.append("X")
        else:
            feedback.append("-")

    # print the feedback for the guess
    print(" ".join(feedback))

# if the loop finishes without guessing the word, print the correct word
if len(guesses) == max_guesses:
    print("Sorry you did not guess the word")
