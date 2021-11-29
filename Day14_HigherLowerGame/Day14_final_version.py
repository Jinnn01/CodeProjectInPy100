import art
import game_data
import random
import replit

# display
print(art.logo)


def play_game():
    # get data from game_data randomly and make sure not same

    Compare_A = random.choice(game_data.data)
    Against_B = random.choice(game_data.data)
    while Compare_A == Against_B:
        Against_B = random.choice(game_data.data)

    print_Astring = f"Compare A: {Compare_A['name']}, {Compare_A['description']}, from {Compare_A['country']}"
    # hint for test
    print(Compare_A['follower_count'], Against_B['follower_count'])
    print_Bstring = f"Against B: {Against_B['name']}, {Against_B['description']}, from {Against_B['country']}"
    print(print_Astring)
    print(art.vs)
    print(print_Bstring)
    # compare data
    if Compare_A['follower_count'] > Against_B['follower_count']:
        result = 1  # means A>B
    else:
        result = -1  # means A<B
    return result


final_score = 0
while True:
    result = play_game()
    # ask uer to input
    user_choice = input("Who has more followers? Type 'A' or 'B':")
    if user_choice == 'A':
        user_choice = 1
    elif user_choice == 'B':
        user_choice = -1

    # check the result
    if result != user_choice:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        break

    else:
        # keep ask asking - while loop
        # score +1
        final_score += 1
        replit.clear()
        print(art.logo)
        print(f"You're right!Current score: {final_score}.")

