from replit import clear
import art

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program!")

# initialise an empty dict{name:bidder}
auction_dict = {}
def sercet_auction():
    # ask user input their name(key)
    key_name = input("What is your name?: ")
    # ask user input their bidder
    input_bidder = input("What's your bid?: $")
    value_bidder = int(input_bidder)
    auction_dict[key_name] = value_bidder
    # ask user whether there is other bidders
    restart = input("Are there any other bidders? Type'yes' or 'no'.")
    clear()
    if restart=="yes":
        sercet_auction()
    else:
        # initial max name and value
        max_name = ""
        max_value = 0
        # get the max value
        for key in auction_dict:
            if auction_dict[key] > max_value:
                max_value=auction_dict[key]
                max_name = key
        print(f"The winner is {max_name} with a bid of ${max_value}")

sercet_auction()