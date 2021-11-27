import art
import random

# greeting
print(art.logo)
print("I'm thinking of a number between 1 and 100.")

# get random number
target_number = random.randint(1, 100)
# help to test
print(f"Pssst, the correct answer is {target_number}")
# ask user to input
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if user_choice == "easy":
    guess_times = 10
else:
    guess_times = 5

while guess_times > 0:
    print(f"You have {guess_times} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if guess_times > 1:
        # < target_number
        if user_guess< target_number:
            print("Too low.")
            print("Guess again.")
        elif user_guess> target_number:
            print("Too high.")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {target_number}.")
            break
    else:
        if user_guess< target_number:
            print("Too low.")
            print("You've run out of guesses, you lose.")
        elif user_guess> target_number:
            print("Too high.")
            print("You've run out of guesses, you lose.")
        else:
            print(f"You got it! The answer was {target_number}.")
            break
    guess_times -=1