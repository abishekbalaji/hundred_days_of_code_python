# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open(file="Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")

with open(file='Input/Letters/starting_letter.docx') as file:
    contents = file.read()

for name in names:
    with open(file=f"Output/ReadyToSend/invite_{name}.docx", mode='w') as file:
        file.write(contents.replace(PLACEHOLDER, name))
