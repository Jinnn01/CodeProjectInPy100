import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# initialise a random list to store all the random elements
random_list = []

# get random letter/symbol/numbers
for i in range(nr_letters):
    random_letter = random.choice(letters)
    random_list.append(random_letter)

for i in range(nr_symbols):
    random_symbol = random.choice(symbols)
    random_list.append(random_symbol)

for i in range(nr_numbers):
    random_num = random.choice(numbers)
    random_list.append(random_num)

# randomly get the element in random list
random_password = "".join(random.sample(random_list,len(random_list)))
print(f"There is your random password:{random_password}")