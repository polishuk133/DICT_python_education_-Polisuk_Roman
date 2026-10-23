import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_letters = set()
lives = 8
print("HANGMAN")
while lives > 0:
    mask = "".join(c if c in guessed_letters else "-" for c in secret_word)
    print(mask)
    if "-" not in mask:
        print("You guessed the word!")
        print("You survived!")
        break
    letter = input("Input a letter: > ")
    if letter in secret_word:
        if letter in guessed_letters:
            print("No improvements")
            lives -= 1
        else:
            guessed_letters.add(letter)
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
else:
    print("You lost!")