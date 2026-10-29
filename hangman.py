import random
words = ['python', 'java', 'javascript', 'php']
def play():
    secret_word = random.choice(words)
    guessed_letters = set()
    lives = 8
    while lives > 0:
        mask = "".join(c if c in guessed_letters else "-" for c in secret_word)
        print(mask)
        if "-" not in mask:
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return
        letter = input("Input a letter: > ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not ("a" <= letter <= "z"):
            print("Please enter a lowercase English letter")
        elif letter in guessed_letters:
            print("You've already guessed this letter")
        elif letter in secret_word:
            guessed_letters.add(letter)
        else:
            guessed_letters.add(letter)
            print("That letter doesn't appear in the word")
            lives -= 1
    print("You lost!")
print("HANGMAN")
while True:
    choice = input('Type "play" to play the game, "exit" to quit: > ')
    if choice == "play":
        play()
    elif choice == "exit":
        break