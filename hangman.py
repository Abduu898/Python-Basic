import random
from english_words import english_words_lower_set

from firstBrick import you_lose
from secondBrick import random_item
from thirdBrick import underscore

WORDS = [w for w in english_words_lower_set if 5 <= len(w) <= 10]

def random_word():
    return random.choice(WORDS)

def show_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display

def play():
    secret = random_word()
    guessed = []
    penalties = 0
    print("Welcome to Hangman!")
    print()

    while True:
        print(show_word(secret, guessed), " || ", penalties,
              "penalty" if penalties == 1 else "penalties")
        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return

        you_lose(penalties)
        if penalties >= 12:
            print("The word was:", secret)
            return

        guess = input(">> ").strip().lower()

        if guess == "":
            continue ## Go Back to the top 

        if len(guess) == 1:
            if guess in guessed:
                print("You already tried", guess.upper())
                continue

            guessed.append(guess)

            if guess in secret:
                print("Found one '" + guess.upper() + "'")
            else:
                penalties = penalties + 1
                print("No '" + guess.upper() + "' found")

        else:
            if guess == secret:
                print(guess.upper() + ": correct guess - " + str(penalties) + " penalties")
                print("You win! The word was:", secret)
                return
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")


play()