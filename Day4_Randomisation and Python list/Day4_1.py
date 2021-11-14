rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

choice_list = [rock, paper, scissors]
# asking user to input

while True:
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_choice = int(user_input)
    print(choice_list[user_choice])

    # 0 rock; 1 paper; 2 scissors
    computer_choice = random.randint(0, 2)

    print("Computer Choose\n", choice_list[computer_choice])

    # status
    status = ""
    if user_choice == 0:
        if computer_choice == 1:
            print("You loose😭")
        elif computer_choice == 2:
            print("You win😊")
        else:
            status = "Tie"
            print("Oops Tie!")

    if user_choice == 1:
        if computer_choice == 2:
            print("You loose😭")
        elif computer_choice == 0:
            print("You win😊")
        else:
            status = "Tie"
            print("Oops Tie!")

    if user_choice == 2:
        if computer_choice == 0:
            print("You loose😭")
        elif computer_choice == 1:
            print("You win😊")
        else:
            status = "Tie"
            print("Oops Tie!")

    if status != "Tie":
        break
    else:
        print()
        print("Try again")
