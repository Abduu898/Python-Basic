import random

themes = {
    "fruits": ["apple", "banana", "cherry", "mango", "orange",
               "grape", "peach", "melon", "lemon", "kiwi"],
    "animals": ["tiger", "elephant", "giraffe", "penguin", "dolphin",
                "kangaroo", "rabbit", "monkey", "zebra", "lion"],
    "code": ["python", "function", "variable", "integer", "boolean",
             "string", "list", "tuple", "dictionary", "loop"],
    "countries": ["france", "brazil", "japan", "canada", "egypt",
                  "india", "mexico", "norway", "kenya", "spain"],
}


def choose_theme():
    print("Available themes:")
    for name in themes:
        print("-", name)
    print("- random")

    choice = input("Choose a theme: ").strip().lower()

    if choice == "random" or choice not in themes:
        choice = random.choice(list(themes.keys()))

    return choice


def max_penalties_for(word):
    p = 6 + (10 - len(word))
    if p < 6:
        p = 6
    if p > 12:
        p = 12
    return p


def show_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display


def play():
    theme = choose_theme()
    words = themes[theme]
    secret = random.choice(words)
    max_penalties = max_penalties_for(secret)

    guessed = []
    penalties = 0

    print()
    print("Theme:", theme)
    print("Max penalties:", max_penalties)
    print()

    while True:
        print(show_word(secret, guessed), " || ", penalties, "penalties")

        won = True
        for letter in secret:
            if letter not in guessed:
                won = False
                break
        if won:
            print("You win! The word was:", secret)
            return

        if penalties >= max_penalties:
            print("You lose! The word was:", secret)
            return

        guess = input(">> ").strip().lower()

        if guess == "":
            continue

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
                print(guess.upper() + ": correct guess")
                print("You win! The word was:", secret)
                return
            else:
                penalties = penalties + 5
                print(guess.upper() + ": incorrect guess")


if __name__ == "__main__":
    play()

    
