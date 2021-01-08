word = "hangman"
guessed_letters = []
count = 6

def get_word(count):
    print(f"You have {count} guesses left!")
    temp_word = ""
    for letter in word:
        if letter in guessed_letters:
            temp_word += letter
        else:
            temp_word += '*'
    return temp_word

def hangman(char, count):
    temp_word = ""
    if not char in guessed_letters:
        guessed_letters.append(char)
        if not char in word:
            count -= 1
            print("That's incorrect.")
            temp_word = get_word(count)
        else:
            print("That's a correct guess!")
            temp_word = get_word(count)
    else:
        print("You have already guessed that letter. Try something else.")
        temp_word = get_word(count)
    return [temp_word, count]
    

while count > 0:
    guess = input("Enter your guess: ")
    [temp_word, count] = hangman(guess, count)
    print(temp_word)
    if temp_word == word:
        print("You have won!")
        break
    elif count == 0:
        print("You have lost.")

    

