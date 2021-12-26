# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_address = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day24_FilesDirectories&Paths/Mail Merge Project Start/Input/Names/invited_names.txt"
with open(name_address, "r") as name_file:
    # get name list
    name_string = name_file.read().split("\n")
    print(name_string)

letter_address = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day24_FilesDirectories&Paths/Mail Merge Project Start/Input/Letters/starting_letter.txt"
with open(letter_address, "r") as letter_file:
    # get letter content
    content = letter_file.read()
    for name in name_string:
        # create new txt file
        with open(f"letter_to_{name}.txt", "w") as inviting_letter:
            # replace the example letter with people name
            rewrite_content = content.replace("[name]", name)
            inviting_letter.write(rewrite_content)
