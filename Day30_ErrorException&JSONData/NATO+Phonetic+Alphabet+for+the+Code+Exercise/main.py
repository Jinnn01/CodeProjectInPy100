# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv(
    "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generator():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please")
        generator()
    else:
        print(output_list)


generator()
