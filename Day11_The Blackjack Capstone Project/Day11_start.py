'''
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
'''
import random


def get_card(list):
    '''
    import a card list
    function to randomly get a card
    and return a card list
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    add_card = random.choice(cards)
    list.append(add_card)
    return list


def initial_card(list):
    for i in range(2):
        list = get_card(list)
    return list


# initialise  cards lists
def get_computer_cards():
    computer_list = []
    computer_list = initial_card(computer_list)
    while sum(computer_list) < 17:
        computer_list = get_card(computer_list)
    return computer_list


def get_user_cards():
    user_card = []
    user_card = initial_card(user_card)
    return user_card


def print_format():
    print(f"Your cards:{user_card},current score:{sum(user_card)}")
    print(f"Computer's first card: {computer_card[0]}")


def print_final():
    print(f"Your cards:{user_card},final score:{sum(user_card)}")
    print(f"Computer's first card: {computer_card},final score:{sum(computer_card)}")


def compare_card(list1, list2):
    if sum(list1) > 21:
        return -1  # -1 == bust
    elif sum(list2) > 21:
        return 2  # 2 = win, Opponent went over. You win
    elif sum(list1) > sum(list2):
        return 1  # 1 == win
    elif sum(list1) == sum(list2):
        return 0  # 0 == dawn
    else:
        return -2  # -1 == lose


def get_result():
    result_flag = compare_card(user_card, computer_card)
    if result_flag == 2:
        print("Opponent went over. You win😁")
    if result_flag == -2:
        print("You lose 😤")
    if result_flag == 0:
        print("Draw 🙃")
    if result_flag == -1:
        print("You went over. You lose 😭")
    if result_flag == 1:
        print("Yon win")


def more_round(user_card):
    while True:
        con_choice = input("Type 'y' to get another card, type 'n' to pass:")
        if con_choice == "n":
            print_final()
            get_result()
            break
        elif con_choice == "y":
            user_card = get_card(user_card)
            if sum(user_card) <= 21:
                print_format()
                more_round(user_card)
            else:
                print_format()
                print_final()
                get_result()
                break
                '''
                testcase:
                Do you want to play a game of Blakjack? Type'y' or 'n':>? y
                Your cards:[7, 3],current score:10
                Computer's first card: 8
                Type 'y' to get another card, type 'n' to pass:>? y
                Your cards:[7, 3, 3],current score:13
                Computer's first card: 8
                Type 'y' to get another card, type 'n' to pass:>? y
                Your cards:[7, 3, 3, 10],current score:23
                Computer's first card: 8
                Your cards:[7, 3, 3, 10],final score:23
                Computer's first card: [8, 2, 11],final score:21
                You went over. You lose 😭
                Type 'y' to get another card, type 'n' to pass:
                '''

        # compare and print


while True:
    start = input("Do you want to play a game of Blakjack? Type'y' or 'n':")
    if start == 'y':
        user_card = get_user_cards()
        computer_card = get_computer_cards()
        print_format()

        # compare_card(user_card,computer_card)
        more_round(user_card)
    if start == "n":
        break
