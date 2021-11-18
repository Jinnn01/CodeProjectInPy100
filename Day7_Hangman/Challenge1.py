# Step 1_Picking a random words and checking answers
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

word_list = ["aardvark", "baboon", "camel"]

# get random word for the list
chosen_word = random.choice(word_list)

# ask user to guess a letter
guess= input("Please guess a letter: ")
# lowercase
guess.lower()

# check the letter is one of the letter in chosen  word
for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
        print("Right")
    else:
        print("Wrong")