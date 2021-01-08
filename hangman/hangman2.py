import random
import hangman_art
import hangman_words

words = hangman_words.word_list
stages = hangman_art.stages
count = len(stages)


def init(count):
    temp_word = []
    word = random.choice(words)
    for _ in word:
        temp_word.append("_")
    count = min(count, len(word))
    print(
        f"The word is {''.join(temp_word)}\nYou have {count} guesses left.")
    return [word, temp_word, count]


def game(guess, word, count, temp_word):
    if guess in temp_word:
        print("You have already guessed it. Try something else.")
    elif guess in word:
        print("That's correct!")
        for i in range(len(word)):
            if guess == word[i]:
                temp_word[i] = guess
    else:
        print("That's incorrect.")
        print(stages[count - 1])
        count -= 1
    return [temp_word, count]


[word, temp_word, count] = init(count)

while count > 0:
    guess = input("Enter a guess: ").lower()
    [temp_word, count] = game(guess, word, count, temp_word)
    temp_word_str = "".join(temp_word)
    if temp_word_str == word:
        print(f"You have won!\nThe word was {word}.")

        break
    elif count == 0:
        print(f"You have lost!\nThe word was {word}.")
    else:
        print(f"{''.join(temp_word)}\nYou have {count} lives left.")
