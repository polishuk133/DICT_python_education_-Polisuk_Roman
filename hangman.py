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
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
        break
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
else:
    print("You lost!")