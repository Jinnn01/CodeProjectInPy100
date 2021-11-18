# Step 2_Replacing Blanks with the guess

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

# get ["_", "_", "_", "_", "_"] replace
# method2
display_str = "_ "*len(chosen_word)
display_lst = display_str[:-1].split(" ")
# method1 we can use for loop ,initial an empty list and append "-"
display=[]
for i in range(len(chosen_word)):
    display+="_"
print(display)


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
        display_lst[i]=guess


# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display_lst)
