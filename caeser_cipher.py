def encode(message, shift):
    cipher = ""
    for letter in message:
        if letter.isalpha():
            ascii_ = ord(letter)
            temp = ascii_ + shift
            if temp > 122:
                char = temp % 123 + 97
            else:
                char = temp
            cipher += str(chr(char))
        else:
            cipher += letter

    return cipher


def decode(message, shift):
    text = ""
    for letter in message:
        if letter.isalpha():
            ascii_ = ord(letter)
            temp = ascii_ - shift
            if temp < 97:
                char = 122 - (96 % temp)
            else:
                char = temp
            text += str(chr(char))
        else:
            text += letter
    return text


# def caeser(message, shift, direction):
#     text = ""
#     for letter in message:
#         if letter.isalpha():
#             ascii_ = ord(letter)
#             if direction == "encode":
#                 temp = ascii_ + shift
#                 if temp > 122:
#                     char = temp % 123 + 97
#                 else:
#                     char = temp
#             else:
#                 temp = ascii_ - shift
#                 if temp < 97:
#                     char = 122 - (96 % temp)
#                 else:
#                     char = temp
#             text += str(chr(char))
#         else:
#             text += letter
#     return text
                
                
            
    


go = "yes"

while go == "yes":
    to_do = ""
    while not to_do in ["encode", "decode"]:
        to_do = input("Type 'encode' to encrypt 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n")) % 26
    if to_do == "encode":
        cipher = encode(message, shift)
        print(f"Encoded message: {cipher}")
    else:
        text = decode(message, shift)
        print(f"Decode message: {text}")
    go = input("Do you wish to continue? Enter 'yes' or 'no': ")
