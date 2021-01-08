import random
import art


def check(guess, num):
    if guess == num:
        print("You win!")
        return 1
    elif guess > num:
        print("Your guess is higher.")
    else:
        print("Your guess is lower.")

def game():
    print("welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print(art.logo)

    num = random.randint(1, 100)

    levels = {
        "easy": 10,
        "hard": 5
    }

    won = False

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guesses = levels[difficulty]
    print(f"You have {guesses} chances to guess the number.")


    for i in range(guesses):
        right_input = False
        while not right_input:
            try:
                guess = int(input("Type your guess: "))
                if guess > 0 and guess < 101:
                    right_input = True
                else:
                    raise ValueError
            except:
                print("Invalid input.")

        if check(guess, num) == 1:
            won = True
            return
        print(f"Number of chances left: {guesses - i - 1}")

    if not won:
        print(f"You lose. The number was {num}.")
        
game()
