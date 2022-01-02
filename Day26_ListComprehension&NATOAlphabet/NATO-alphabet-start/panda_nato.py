import pandas

# Create a dictionary in this format:
file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day26_ListComprehension&NATOAlphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv"
data = pandas.read_csv(file_path)
letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word: ")
word_list = [letter.capitalize() for letter in user_input]
# letter in word list get the value of that letter key
phonetic_list = [letter_dict[letter] for letter in word_list]
print(phonetic_list)